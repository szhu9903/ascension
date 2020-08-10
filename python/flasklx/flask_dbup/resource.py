
from flask import Flask
from flask_login import LoginManager
import sys,os


dev = sys.argv[1]
if dev == 'run':
    from config.config import *
elif dev == 'dev':
    from config.dev_config import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

login_message = LoginManager()
login_message.login_view = 'login'
login_message.init_app(app)


from views.login_controller import *
