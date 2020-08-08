PROFILE_FILE = "profile.json"

from flask import Flask
from flask_wtf.csrf import CsrfProtect
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '9a571858-4c78-4bc0-b6d6-8fdda031fecf'



# 配置用户登录
login_message = LoginManager()
login_message.session_protection = 'strong'
# login_required 验证失败 跳转到login
login_message.login_view = 'login'
login_message.init_app(app)




csrf = CsrfProtect()
csrf.init_app(app)



from view.login_controller import *





