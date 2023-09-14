import socket
import json
DISCONNECT_MSG="exit"
with open('config.json') as config_file:
    config = json.load(config_file)
    host = config['server_address1']
    port = config['port1']
def server_message():
    server = socket.socket()
    server.bind((host,port))
    server.listen(1)
    print("server1 is listening....")
    client_socket, client_address = server.accept()
    print(f"connected to {client_address}")
    connected = True
    while connected :
        data = client_socket.recv(1024).decode()
        #if not data:
            #break
        print(f"clint: {data}")
        message = input("server1: ")
        if message==DISCONNECT_MSG:
            connected =False
        else:
            client_socket.send(message.encode())
    client_socket.close()
    server.close()
if __name__ == "__main__":
    server_message()
