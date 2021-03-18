import queue
from threading import Thread
import random,time

queue = queue.Queue(10)

class Producer(Thread):
    def run(self):
        while True:
            elem = random.randrange(9)
            queue.put(elem)
            print('put%s'%elem)
            time.sleep(random.randint(3,5))
class Consumer(Thread):
    def run(self):
        while True:
            elem = queue.get()
            print('g%s'%elem)
            time.sleep(random.randint(2,4))

if __name__ == '__main__':
    p = Producer()
    p.start()
    c = Consumer()
    c.start()

