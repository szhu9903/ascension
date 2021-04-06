
from . import main

@main.route('/', methods=['GET', 'POST'])
def main_log():
    return 'test'

