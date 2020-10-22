import socket
import logging

SOCKET_HOST = "localhost"
SOCKET_PORT = 8080



def main():
    with socket.socket() as socket_server:
        socket_server.bind((SOCKET_HOST,SOCKET_PORT))
        socket_server.listen()
        print("开始监听(%s:%s)"%(SOCKET_HOST,SOCKET_PORT))
        # 利用循环开启，夯住
        socket_con, add = socket_server.accept()
        while True:
            name = socket_con.recv(1024).decode('utf-8')
            socket_con.send(('echo %s'%name).encode('utf-8'))


if __name__ == '__main__':
    main()