import socket
from bullscode import BullsCode
def game():
    my_socket = (socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect("192.168.1.27", 12345)
    t = 0
    while (t != 11):
        gess = input("enter your gess")
        my_socket.send(gess.encode())
        result = my_socket.recv(1024).decode()
        print("the server sent" + result)
        if (result == ['B', 'B', 'B', 'B']):
            print("win")
            break
        t+=1
    else:
        print("loose")
    my_socket = socket.close()
if __name__ == "__game__":
    game()