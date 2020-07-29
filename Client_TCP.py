import socket
import sys

NETWORK_ADDRESS = "127.0.0.1"
PORT_NUMBER = 40000


def connect_to_server(server_address, port_number):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_address, port_number))
    except socket.error as socket_error:
        print("Error while trying to connect to {}!\n\n".format(server_address))
        print(socket_error)
        print("\n\n")
        sys.exit()
    return client

def send(client,data):
    client.send(str.encode(data))

def get_response(client):
    return client.recv(4096)

if __name__ == "__main__":
    my_client = connect_to_server(NETWORK_ADDRESS, PORT_NUMBER)
    while True:
        message = input("Insert command here: ")
        send(my_client, message)
        response = get_response(my_client).decode()
        print(response)
        if response.lower() == "rst":
            break
