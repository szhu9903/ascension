import socket
import logging

SOCKET_HOST = "localhost"
SOCKET_PORT = 8080



def main():
    with socket.socket() as socket_server:
        socket_server.bind((SOCKET_HOST,SOCKET_PORT))
        socket_server.listen()
        print("开始监听(%s:%s)"%(SOCKET_HOST,SOCKET_PORT))
        socket_con, add = socket_server.accept()
        print("HELLO %s"%add)
        with socket_con as socket_cli:
            data = socket_cli.recv()
            socket_cli.send('【echo】%s'%data)


if __name__ == '__main__':
    main()