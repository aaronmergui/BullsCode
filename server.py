import socket
import random
from bullscode import BullsCode
def game():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind('0.0.0.0',12345)
    server_socket.listen()
    print("server listening")
    client_socket,client_adress=server_socket.accept()
    print("player connected")
    t=0
    while True:
        random_answer=BullsCode(random.randint(0,9999))
        while(t!=11):
            client_gess=client_socket.recv(1024).decode()
            result=random_answer.check(client_gess)
            client_socket.send(result.encode())
            if(result==["'B', 'B', 'B', 'B'"]):
                print("player won ")
                break
            t+=1
        else:
            print("Computer won!")
        client_socket.close()

if __name__ == "__game__":
    game()



























