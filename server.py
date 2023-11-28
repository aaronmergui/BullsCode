import socket
import random
from bullscode import BullsCode

ADDRESS = "0.0.0.0"
PORT = 2289


def game():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ADDRESS, PORT))
    server_socket.listen()
    print("server listening")
    client_socket, client_adress = server_socket.accept()
    print("player connected")
    t = 0
    random_answer = BullsCode()
    while t != 10:
        client_gess = client_socket.recv(1024).decode()
        result = random_answer.check(BullsCode(client_gess))
        result = ''.join(result)
        client_socket.send(result.encode())
        if result == "BBBB":
            print("player won ")
            break
        if t == 9:
            print("Computer won!")
        t += 1

    client_socket.close()


if __name__ == '__main__':
    game()
