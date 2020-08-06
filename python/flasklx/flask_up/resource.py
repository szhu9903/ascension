from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '9a571858-4c78-4bc0-b6d6-8fdda031fecf'



PROFILE_FILE = "profile.json"

from view.login_controller import *





