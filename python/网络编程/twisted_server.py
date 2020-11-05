from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor
from twisted.python import log
import struct

protocolList = []

class GeneriProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.listen_host = None
        self.listen_port = None

    # 连接建立时调用，级在accept()停止阻塞开始接收套接字时执行，欢迎消息应该在此处发送
    def connectionMade(self):
        # 获取连接地址
        self.listen_host = self.transport.getPeer().host
        self.listen_port = self.transport.getPeer().port
        # 发送初始消息
        self.transport.write(struct.pack("!h", 12))

    # 接收到消息时调用
    def dataReceived(self, data):
        print("data ---->%s"%data)

    # 当连接关闭时调用清除连接
    def connectionLost(self, reason):
        if self in protocolList:
            protocolList.remove(self)
        # 强制关闭
        self.transport.abortConnection()

# 连接生产工厂 Factory创建一个Protocol实例，并将该实例的factory属性指向自己
class GenericFactor(Factory):
    def buildProtocol(self, addr):
        newProtocol = GeneriProtocol(self)
        protocolList.append(newProtocol)
        return newProtocol


if __name__ == '__main__':
    log.msg('start twisted ...')
    reactor.listenTCP(8000, GenericFactor())
    reactor.run()


