import socket

SOCKET_HOST = "localhost"
SOCKET_PORT = 8080
def main():
    with socket.socket() as client_socket:
        client_socket.connect((SOCKET_HOST,SOCKET_PORT))
        while True:
            name = input('name :')
            client_socket.send(name.encode('utf-8'))
            server_name = client_socket.recv(1024)
            print(server_name.decode('utf-8'))
main()