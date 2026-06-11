from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# Store connected clients
clients = {}
addresses = {}

# Server configuration
HOST = ""
PORT = 33000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

# Create TCP socket
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDRESS)


def accept_connections():
    """
    Accept new users joining the chat.
    """
    while True:
        client, client_address = SERVER.accept()
        print(f"{client_address} connected.")

        client.send(
            bytes("Welcome! Enter your username:", "utf8")
        )

        addresses[client] = client_address

        Thread(
            target=handle_client,
            args=(client,)
        ).start()


def handle_client(client):
    """
    Handle a single client's messages.
    """

    name = client.recv(BUFSIZE).decode("utf8")

    welcome = (
        f"Welcome {name}! Type {{quit}} to leave."
    )

    client.send(
        bytes(welcome, "utf8")
    )

    broadcast(
        bytes(f"{name} has joined the chat!", "utf8")
    )

    clients[client] = name

    while True:
        msg = client.recv(BUFSIZE)

        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + ": ")

        else:
            client.send(
                bytes("{quit}", "utf8")
            )

            client.close()

            del clients[client]

            broadcast(
                bytes(f"{name} has left the chat.", "utf8")
            )

            break


def broadcast(message, prefix=""):
    """
    Send a message to all users.
    """

    for user_socket in clients:
        user_socket.send(
            bytes(prefix, "utf8") + message
        )


if __name__ == "__main__":

    SERVER.listen(5)

    print("Server started...")
    print(f"Listening on port {PORT}")

    ACCEPT_THREAD = Thread(
        target=accept_connections
    )

    ACCEPT_THREAD.start()

    ACCEPT_THREAD.join()

    SERVER.close()