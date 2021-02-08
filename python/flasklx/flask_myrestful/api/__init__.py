
from flask import Blueprint


user = Blueprint('user', __name__)
from .userController import *

main = Blueprint('main', __name__)
from .requestController import *

