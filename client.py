from vidstream import StreamingServer
import threading
import socket
import keyboard

def connectSocket(ip, port):
    client = StreamingServer(ip, port)
    thread = threading.Thread(target=client.start_server)
    thread.start()
    #client.__server_socket.sendall("H")
    return client

def sendInputs(client):
    
    return



def main():
    prompt = input("Type ' connect [address] ' to start viewing (F9 to stop).\n ")
    ip = prompt.split(" ")[1]

    client = connectSocket(ip, 4242)
    sendingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while not keyboard.is_pressed('f9'):
        continue
    client.stop_server()



if __name__ == "__main__" :
    main()


    