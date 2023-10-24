from vidstream import StreamingServer
import threading
import keyboard

def connectSocket(ip, port):
    client = StreamingServer(ip, port)
    thread = threading.Thread(target=client.start_server)
    thread.start()
    return client



def main():
    prompt = input("Type ' connect [address] ' to start viewing (F9 to stop).\n ")
    ip = prompt.split(" ")[1]

    client = connectSocket(ip, 4242)

    while not keyboard.is_pressed('f9'):
        continue
    client.stop_server()



if __name__ == "__main__" :
    main()


    