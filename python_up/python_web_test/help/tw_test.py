# 连接处理
from twisted.internet.protocol import Protocol
# 持久化数据工厂
from twisted.internet.protocol import Factory
# 服务启动器，建立侦听
from twisted.internet import reactor
from help import logger
import time

# 模拟业务处理函数
def time_con(data, protocol):
    time.sleep(10)
    protocol.transport.write(('[ECHO]----> %s' % data).encode('utf-8'))
    return


class GenericProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        host = self.transport.getPeer().host
        port = self.transport.getPeer().port
        type = self.transport.getPeer().type
        connection_message = 'Client %s:%s %s' % (host, port, type)
        logger.info(connection_message)
        self.transport.write(connection_message.encode('utf-8'))

    def dataReceived(self, data):
        # 接收到数据，去执行对应的函数
        reactor.callInThread(time_con, data, self)

    def connectionLost(self, reason):
        # 强制关闭
        self.transport.abortConnection()


class GenericFactory(Factory):
    def buildProtocol(self, addr):
        newProtocol = GenericProtocol(self)
        return newProtocol

if __name__ == '__main__':
    logger.info('Start Twisted service')
    reactor.listenTCP(8080, GenericFactory())
    reactor.suggestThreadPoolSize(10)
    reactor.run()


