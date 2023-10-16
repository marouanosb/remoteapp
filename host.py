import socket
from vidstream import StreamingServer


def openSocket(ip, port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(ip, port)
    serversocket.listen(1)
    return serversocket


if __name__ == "main" :

    while input("Type ' host ' to start hosting.\n> ") != 'host':
        continue

    ip = socket.gethostbyname(socket.gethostname())
    print(f"Started hosting @{ip}")
    serversocket = openSocket(ip, 4242)

