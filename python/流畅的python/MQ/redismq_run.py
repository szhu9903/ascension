
from flask import Flask,redirect
import redis,random,logging

app = Flask(__name__)
app.config['SECRET_KEY'] = '1233'

rcon = redis.StrictRedis(host='47.102.40.50',port=6379,password='1017',db=2)
prodcons_queue = 'prodcons:queue_name'
pubsub_channel = 'pubsub:channel_name'


@app.route('/')
def index():
    html = """
    <br>
    <center><h3> Redis Message Queue </h3>
    <br>
    <a href='/prodcons'>消费者模式</a>
    <br>
    <br>
    <a href='/pubsub'>发布-订阅模式</a>
    </center>
    """
    return html

@app.route('/prodcons')
def prodcons():
    elem = random.randrange(10)
    rcon.lpush(prodcons_queue,elem)
    logging.info("lpush %s--%s "%(prodcons_queue,elem))
    print("lpush %s--%s "%(prodcons_queue,elem))
    return redirect('/')

@app.route('/pubsub')
def pubsub():
    # 创建订阅对象
    ps = rcon.pubsub()
    # 订阅
    ps.subscribe(pubsub_channel)
    # 消息发布
    elem = random.randrange(10)
    rcon.publish(pubsub_channel,elem)
    return redirect('/')


if __name__ == '__main__':
    app.run('127.0.0.1',5000,debug=True)

