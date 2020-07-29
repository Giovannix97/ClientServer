import socket
import threading
import sys

NETWORK_ADDRESS = "127.0.0.1"
PORT_NUMBER = 40000
NUMBER_CONNECTIONS = 5

def initialize_server(address, port_number, number_of_connections):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((address, port_number))
    server.listen(number_of_connections)
    print("[*] listening on %s:%d" % (address,port_number))
    return server

def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        request = request.decode()
        print("[*] Receveid %s" % request)


        exit_words = ["end", "exit", "esc", "bye"]

        if str(request.lower()) in exit_words:
            client_socket.send(str.encode("RST"))
            client_socket.close()
            print("[*] Connection closed with %s:%d" % (addr[0], addr[1]))
            break
        else:
            client_socket.send(str.encode("ACK"))


if __name__ == "__main__":
    print("Welcome to this server")

    my_server = initialize_server(NETWORK_ADDRESS, PORT_NUMBER, NUMBER_CONNECTIONS)

    while True:
        client, addr = my_server.accept()
        print("[*] Accepted new connection from %s:%d" % (addr[0], addr[1]))

        client_handler = threading.Thread(
            target=handle_client,
            args=(client,)
        )
        client_handler.start()
