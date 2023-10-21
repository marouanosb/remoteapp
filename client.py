from vidstream import ScreenShareClient

def connectSocket(ip, port):

    return True


def main():
    prompt = input("Type ' connect [address] ' to start viewing.\n ")
    ip = prompt.split(" ")[1]
    print(ip)

    connection = connectSocket(ip, 4242)

if __name__ == "__main__" :
    main()


    