
from resource import  app
from wtf.login import LoginForm
from flask import render_template



@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='登录',form=form)


