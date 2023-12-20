import socket
from bullscode import BullsCode
import time
IP_ADRESS = " 192.168.1.27"
IP_LOCAL = "127.0.0.1"
PORT = 2289


def game():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP_LOCAL, PORT))
    t = 0
    start=0
    win = False
    while t != 10 or win == True:
        gess = input("enter your guess: ")
        if t==0:
            start=time.time()
        my_socket.send(gess.encode())
        result = my_socket.recv(1024).decode()
        if result == "close":
            break
        print("the server sent: " + result)
        if (result == "[B, B, B, B]"):
            print("win")
            win = True
        if t == 9:
            print("loose")
        t += 1
        if time.time()-start>=30:
            break

        while win == True:
            continue

    my_socket.send("".encode())
    my_socket.close()


if __name__ == '__main__':
    game()
