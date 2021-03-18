# http 基于tcp的封装实现，需引用socket实现
import socket
import multiprocessing

class httpServer(object):
    def __init__(self, port):
        # SOCK_STREAM(数据流): 基于TCP;
        # SOCK_DGRAM(数据包):是基于UDP的
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置核心端口
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_server.bind(("0.0.0.0", port))
        self.socket_server.listen()

    def start(self):
        while True:
            client_socket, client_address = self.socket_server.accept()
            print('新的连接 ip: %s 端口：%s' % client_address)
            client_process = multiprocessing.Process(target = self.handle_response, args=(client_socket,))
            client_process.start()

    def handle_response(self, client_socket):
        request_handle = client_socket.recv(1024)
        print('客户端请求头%s'%request_handle.decode())
        response_start = "HTTP/1.1 200 OK \r\n"
        response_handle = "Server: Zhu Server \r\n Content_Type:text/html \r\n"
        response_body = """
            <html>
                <head>
                    <title>szhu</title>
                    <meta charset='UTF-8'>
                </head>
                <body>
                    <h1>szhu</h1>
                </body>
            </html>
        """
        response = response_start + response_handle + response_body
        client_socket.send(bytes(response, "UTF-8"))
        client_socket.close()

def main():
    port = 8080
    socket_server = httpServer(port)
    socket_server.start()



if __name__ == '__main__':
    main()

