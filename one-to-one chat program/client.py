import socket
import json
DISCONNECT_MSG="exit"
with open('config.json') as config_file:
    config = json.load(config_file)
    host = config['server_address']
    port = config['port']
def client_message():
    client=socket.socket()
    client.connect((host,port))
    connected = True
    while connected:
        message=input("client: ")
        client.send(message.encode())
        if message==DISCONNECT_MSG:
            connected = False
        else:
            data=client.recv(1024).decode()
            print(f"server:{data}")
    client.close()
if __name__ == "__main__":
    client_message()
