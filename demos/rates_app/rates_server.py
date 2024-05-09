"""rate server module"""

from typing import Optional
import multiprocessing as mp
import sys
import socket
import threading

# Create "ClientConnectionThread" class that inherits from "Thread"

# Each time a client connects, a new thread should be created with the
# "ClientConnectionThread" class. The class is responsible for sending the
# welcome message and interacting with the client, echoing messages

# The server should support multiple clients at the same time


class ClientConnectionThread(threading.Thread):
    def __init__(self, conn: socket.socket) -> None:
        threading.Thread.__init__(self)
        self.__conn = conn

    def run(self) -> None:
        # conn.sendall("Connected to the Rates Server".encode("UTF-8"))
        self.__conn.sendall(b"Connected to the Rates Server")

        while True:
            message = self.__conn.recv(2048).decode("UTF-8")

            if not message:
                break

            print(f"recv: {message}")
            self.__conn.sendall(message.encode("UTF-8"))


def rate_server(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:
        socket_server.bind((host, port))
        socket_server.listen()

        print(f"server is listening on {host}:{port}")

        while True:
            conn, addr = socket_server.accept()
            print(f"client from {addr} connected")
            a_thread = ClientConnectionThread(conn)
            a_thread.start()


def command_start_server(
    server_process: mp.Process | None, host: str, port: int
) -> mp.Process:
    """command start server"""

    if server_process and server_process.is_alive():
        print("server is already running")
    else:
        # step 1 - create a new process object to start the rates server
        server_process = mp.Process(target=rate_server, args=(host, port))
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


def main() -> None:
    """Main Function"""

    try:
        host = "127.0.0.1"
        port = 5050
        server_process: Optional[mp.Process] = None

        while True:
            command = input("> ")

            if command == "start":
                server_process = command_start_server(
                    server_process, host, port
                )
            elif command == "stop":
                server_process = command_stop_server(server_process)
            # step 3 - add a command named "status" that outputs to the
            # console if the server is current running or not
            # hint: follow the command function pattern used by the other
            # commands
            elif command == "status":
                command_server_status(server_process)
            elif command == "exit":
                # step 4 - terminate the "server_process" if the
                # "server_process" is an object and is alive
                if server_process and server_process.is_alive():
                    server_process.terminate()
                break

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
