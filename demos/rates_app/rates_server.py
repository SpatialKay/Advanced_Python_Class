"""rate server module"""

from typing import Optional, cast
import multiprocessing as mp
from multiprocessing.sharedctypes import Synchronized
import sys
import socket
import threading
import re
import requests
import logging

from rates_app.database import SessionLocal, engine, Base

from rates_app.models import ExchangeRate


# Task 1 - Cache Rate Results

# Upgrade the application to check the database for a given exchange rate
# (date, currency) - Store the date as a string, currency symbol as a string
# and the currency value as a float.

# If the exchange rate was previously retrieved and stored in the
# database (inside the rates table), then return it

# If the exchange rate is not in the database, then download it (get it from
# the Rates API), add it to the database and return it

# Task 2 - Clear Rate Cache

# Add a command for clearing the rate cache from the server command
# prompt. Name the command "clear".


client_command_pattern = (
    r"^(?P<command_name>[A-Z]+) "
    r"(?P<market_date>[0-9]{4}-[0-9]{2}-[0-9]{2}) "
    r"(?P<currency_symbol>[A-Z]{3})$"
)


class InvalidCommandError(Exception):
    def __init__(self, command: str) -> None:
        super().__init__(
            (
                f"User entered command {command} does not match the "
                f"following pattern COMMAND_NAME YYYY-MM-DD CURRENY_SYMBOL"
            )
        )


class InvalidCommandNameError(Exception):
    def __init__(
        self, requested_command_name: str, available_command_names: list[str]
    ) -> None:
        super().__init__(
            (
                f"User entered command {requested_command_name} "
                "is not in the list "
                f"of available commands {available_command_names}"
            )
        )


class ClientConnectionThread(threading.Thread):
    def __init__(self, conn: socket.socket, counter: Synchronized) -> None:
        threading.Thread.__init__(self)
        self.__conn = conn
        self.__command_names = ["GET"]
        self.__client_command_regex = re.compile(client_command_pattern)
        self.__counter = counter

    def parse_client_command(self, command: str) -> tuple[str, str, str]:
        command_match = self.__client_command_regex.match(command)

        if not command_match:
            raise InvalidCommandError(command)

        command_parts_dict = command_match.groupdict()
        command_name = command_parts_dict["command_name"]
        market_date = command_parts_dict["market_date"]
        currency_symbol = command_parts_dict["currency_symbol"]

        return command_name, market_date, currency_symbol

    def process_client_command(
        self, command_name: str, market_date: str, currency_symbol: str
    ) -> str:
        if command_name not in self.__command_names:
            raise InvalidCommandNameError(command_name, self.__command_names)

        with SessionLocal() as db_session:
            exchange_rate = (
                db_session.query(ExchangeRate)
                .filter_by(
                    market_date=market_date, currency_symbol=currency_symbol
                )
                .first()
            )

            if exchange_rate:
                return f"{currency_symbol}: {exchange_rate.currency_rate}"

        resp = requests.get(
            (
                "http://127.0.0.1:8080"
                f"/api/{market_date}"
                f"?base=USD&symbols={currency_symbol}"
            ),
            timeout=60,
        )

        currency_rate = float(resp.json()["rates"][currency_symbol])

        with SessionLocal() as db_session:
            exchange_rate = ExchangeRate(
                market_date=market_date,
                currency_symbol=currency_symbol,
                currency_rate=currency_rate,
            )
            db_session.add(exchange_rate)
            db_session.commit()

        return f"{currency_symbol}: {currency_rate}"

    def run(self) -> None:
        # conn.sendall("Connected to the Rates Server".encode("UTF-8"))
        self.__conn.sendall(b"Connected to the Rates Server")

        while True:
            command = self.__conn.recv(2048).decode("UTF-8")

            if command == "count":
                self.__conn.sendall(
                    f"{self.__counter.value} connected clients".encode("UTF-8")
                )
                continue

            if not command or command == "exit":
                break

            try:
                response = self.process_client_command(
                    *self.parse_client_command(command)
                )

            except InvalidCommandError as exc:
                logging.log(logging.INFO, "Invalid Command", exc_info=exc)
                response = "Invalid Command"
            except InvalidCommandNameError as exc:
                logging.log(logging.INFO, "Invalid Command Name", exc_info=exc)
                response = "Invalid Command Name"
            except Exception as exc:
                logging.log(logging.ERROR, "Unknown Error", exc_info=exc)
                response = "Unknown Error"

            finally:
                self.__conn.sendall(response.encode("UTF-8"))

        with self.__counter.get_lock():
            self.__counter.value -= 1


def rate_server(host: str, port: int, counter: Synchronized) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:
        socket_server.bind((host, port))
        socket_server.listen()

        print(f"server is listening on {host}:{port}")

        while True:
            conn, addr = socket_server.accept()
            print(f"client from {addr} connected")
            a_thread = ClientConnectionThread(conn, counter)
            a_thread.start()

            with counter.get_lock():
                counter.value += 1


def command_start_server(
    server_process: mp.Process | None,
    host: str,
    port: int,
    counter: Synchronized,
) -> mp.Process:
    """command start server"""

    if server_process and server_process.is_alive():
        print("server is already running")
    else:
        # step 1 - create a new process object to start the rates server
        server_process = mp.Process(
            target=rate_server, args=(host, port, counter)
        )
        # step 2 - start the new process object
        server_process.start()
        print("server started")

    return server_process


def command_stop_server(
    server_process: Optional[mp.Process],
) -> Optional[mp.Process]:
    """command stop server"""

    if not server_process or not server_process.is_alive():
        print("server is not running")
    else:
        server_process.terminate()
        print("server stopped")

    return None


def command_server_status(server_process: mp.Process | None) -> None:
    """command server status"""

    if server_process and server_process.is_alive():
        print("server is running")
    else:
        print("server is not running")


def command_client_count(counter: Synchronized) -> None:
    print(f"{counter.value} connected clients")


def command_clear_cache() -> None:
    with SessionLocal() as db_session:
        db_session.query(ExchangeRate).delete()
        db_session.commit()
        print("cache cleared")


def main() -> None:
    """Main Function"""

    Base.metadata.create_all(bind=engine)

    try:
        host = "127.0.0.1"
        port = 5050
        server_process: Optional[mp.Process] = None
        counter: Synchronized = cast(Synchronized, mp.Value("i", 0))

        while True:
            command = input("> ")

            match command:
                case "start":
                    server_process = command_start_server(
                        server_process, host, port, counter
                    )
                case "stop":
                    server_process = command_stop_server(server_process)
                case "status":
                    command_server_status(server_process)
                case "count":
                    command_client_count(counter)
                case "clear":
                    command_clear_cache()
                case "exit":
                    if server_process and server_process.is_alive():
                        server_process.terminate()
                    break
                case _:
                    print("Invalid Command")

    except KeyboardInterrupt:
        # step 5 - terminate the "server_process" if the
        # "server_process" is an object and is alive
        if server_process and server_process.is_alive():
            server_process.terminate()
        pass

    sys.exit(0)


# to run the program, change into the `demos` folder, then
# run the following command:
# python -m rates_app.rates_server


if __name__ == "__main__":
    main()
