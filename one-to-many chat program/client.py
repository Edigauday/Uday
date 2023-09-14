import socket
import json

DISCONNECT_MSG = "exit"

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    host1 = config['server_address1']
    port1 = config['port1']
    host2 = config['server_address2']
    port2 = config['port2']


def main():
    server1 = (host1, port1)
    server2 = (host2, port2)

    client_scoket1 = socket.socket()
    client_scoket2 = socket.socket()
    client_scoket1.connect(server1)
    client_scoket2.connect(server2)

    connected = True
    while connected:
        message = input("client: ")

        client_scoket1.send(message.encode())
        client_scoket2.send(message.encode())

        if message == DISCONNECT_MSG:
            connected = False
        else:
            data1 = client_scoket1.recv(1024).decode()
            print(f"server1:{data1}")
            data2 = client_scoket2.recv(1024).decode()
            print(f"server2:{data2}")
    client_scoket1.close()
    client_scoket2.close()


if __name__ == "__main__":
    main()
