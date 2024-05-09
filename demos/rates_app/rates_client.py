import socket
import sys


def rate_client(host: str, port: int) -> None:
    try:
        with socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        ) as socket_client:
            socket_client.connect((host, port))

            welcome_message_bytes = socket_client.recv(2048)

            welcome_message = welcome_message_bytes.decode("UTF-8")

            print(welcome_message)

            while True:
                command = input("> ")

                if command == "exit":
                    break
                else:
                    socket_client.sendall(command.encode("UTF-8"))
                    print(socket_client.recv(2048).decode("UTF-8"))

    except ConnectionResetError:
        print("Server connection was closed.")
    except KeyboardInterrupt:
        pass

    sys.exit(0)


if __name__ == "__main__":
    rate_client("127.0.0.1", 5050)
