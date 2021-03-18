import redis

class Task():
    def __init__(self):
        self.rcon = redis.StrictRedis(host='47.102.40.50', port=6379, password='1017', db=2)
        self.queue = 'prodcons:queue_name'

    def listen_task(self):
        while True:
            task = self.rcon.blpop(self.queue)
            print('Task get',task)


if __name__ == '__main__':
    print('开启队列监听')
    Task().listen_task()












