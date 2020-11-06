from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor
import logging
import struct
import time

def init_log():
    # 初始化日志
    applog = logging.getLogger('twisted log')
    applog.setLevel(logging.DEBUG)
    # 定义 Handler ,设置Handler的属性
    appHandler = logging.StreamHandler()
    appFormatter = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")
    appHandler.setLevel(logging.DEBUG)
    appHandler.setFormatter(appFormatter)
    # 初始化完成的Handler 添加进applog
    applog.addHandler(appHandler)

logger = logging.getLogger('twisted log')

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
        logger.info("data ---->%s"%data)

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


# 执行任务 模拟发送消息操作，
def time_sleep_test():
    while True:
        try:
            now_time = time.time()
            t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now_time))
            logger.info("NOW DATE " + t)
        except Exception as err:
            logger.error(err)
        time.sleep(60)


# 为任务开启新的线程，可以将耗时任务集中在此处执行，例如处理发送消息等
def time_start_sleep():
    reactor.callInThread(time_sleep_test)


# 可以在此处定义延时执行任务的顺序，延时执行时间
def repeat_task_set():
    reactor.callLater(2, time_start_sleep)


if __name__ == '__main__':
    # 初始化日志
    init_log()
    logger.info('start twisted ...')
    reactor.listenTCP(8000, GenericFactor())
    # 设置线程池大小，默认值为(5-10)
    reactor.suggestThreadPoolSize(20)
    repeat_task_set()
    reactor.run()


