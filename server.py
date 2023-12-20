import socket
import select

from bullscode import BullsCode

ADDRESS = "0.0.0.0"
PORT = 2289


class Player:
    def __init__(self, socket,address):
        self.socket = socket
        self.address = address
        self.win=False
        self.attempts = 0

def print_client_sockets(client_sockets):
     for c in client_sockets:
         print("\t", c.getpeername())
def client_gestion(player,random_answer,client_guess):

        result = random_answer.check(BullsCode(client_guess))
        result = "[" + ', '.join(result) + "]"
        player.socket.send(result.encode())
        if result == "[B, B, B, B]":
            print("player won ")
            player.win=True
            player.attempts += 1
            return True
        if player.attempts == 9:
            print("Computer won!")
        player.attempts+=1
        return False

def find_player(players,socket):
    for player in players:
        if player.socket == socket:
            return player

def game():
    print("Setting up server...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ADDRESS, PORT))
    server_socket.listen()
    print("server listening")
    players=[]
    client_sockets=[]
    random_answer=BullsCode()
    print(random_answer.code)

    while True:
        ready_to_read, _ready_to_write, _in_error = select.select([server_socket]+ client_sockets, [], [])
        for  ready_socket in ready_to_read:
            if ready_socket == server_socket:
                client_socket, client_address = server_socket.accept()
                print(f"new Player connected  {client_address}")
                new_player = Player(client_socket, client_address)
                players.append(new_player)
                client_sockets.append(client_socket)
                print_client_sockets(client_sockets)

            else:
                print("Data from a client arrived")
                player= find_player(players, ready_socket)
                data = ready_socket.recv(1024).decode()

                if data=="":
                    print("connection closed")
                    client_sockets.remove(ready_socket)
                    players.remove(player)
                    ready_socket.close()
                else:
                    if client_gestion(player,random_answer,data)==True:
                        for x in players:
                            if x!=player:
                                x.socket.send("close".encode())
                                x.socket.close()
                                players.remove(x)
                                client_sockets.remove(x.socket)
                                print("connection closed")




if __name__ == '__main__':
    game()
