import socket
from vidstream import ScreenShareClient
import threading
import keyboard


def startStreaming(ip, port):
    streamer = ScreenShareClient(ip, port)
    thread = threading.Thread(target=streamer.start_stream)
    thread.start()
    return streamer

def main():
    while input("Type ' host ' to start hosting (F9 to stop).\n> ") != 'host' :
        continue

    ip = socket.gethostbyname(socket.gethostname())
    print(f"Started hosting @{ip}")
    streamer = startStreaming(ip, 4242)

    while not keyboard.is_pressed('f9'):
        continue
    streamer.stop_stream()
    

if __name__ == "__main__" :
    main()

