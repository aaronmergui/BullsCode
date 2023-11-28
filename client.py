import socket
from bullscode import BullsCode

IP_ADRESS = "192.168.1.27"
IP_LOCAL = "127.0.0.1"
PORT = 2289


def game():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP_LOCAL, PORT))
    t = 0
    while t != 10:
        gess = input("enter your guess: ")
        my_socket.send(gess.encode())
        result = my_socket.recv(1024).decode()
        print("the server sent: " + result)
        if (result == "BBBB"):
            print("win")
            break
        if t == 9:
            print("loose")
        t += 1

    my_socket.close()


if __name__ == '__main__':
    game()
