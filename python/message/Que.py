import random
import time
from threading import Thread
import queue
import redis

qu = queue.Queue(10)

class Put(Thread):
    def run(self):
        while True:
            elem = random.randrange(9)
            qu.put(elem)
            print('%s--%s--%s'%(self.name,elem,qu.qsize()))
            time.sleep(random.random())

class Get(Thread):
    def run(self):
        while True:
            elem = qu.get()
            print('%s--%s--%s--get'%(self.name,elem,qu.qsize()))
            time.sleep(1)

def main():
    for i in range(3):
        p = Put()
        p.start()
    for i in range(2):
        g = Get()
        g.start()


if __name__ == '__main__':
    main()


