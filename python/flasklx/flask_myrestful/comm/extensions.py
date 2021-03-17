from flask_login import LoginManager


login_message = LoginManager()



# login_message.login_view = 'index'
login_message.session_protection = 'strong'
