import redis

class Task():
    def __init__(self):
        self.rcon = redis.StrictRedis(host='47.102.40.50',port=6379,password='1017',db=2)
        self.ps = self.rcon.pubsub()
        self.ps.subscribe('pubsub:channel_name')

    def listen_task(self):
        for i in self.ps.listen():
            if i['type'] == 'message':
                print("task get",i['data'])

if __name__ == '__main__':
    print('监听')
    Task().listen_task()

