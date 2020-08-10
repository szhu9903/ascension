from  resource import app,login_message
from flask import request,render_template,redirect,url_for
from flask_login import login_user,logout_user,login_required,current_user
from helper.db_helper import getSelect
from lib.User import User

@login_message.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
@app.route('/index',methods=['GET'])
@login_required
def index():
    user = current_user
    return render_template('index.html',user_name=current_user.user_name)

@app.route('/login',methods=['POST','GET'])
def login():
    user_name = request.form.get('user_name','')
    user_pwd = request.form.get('user_pwd','')
    if user_name:
        user = User(user_name)
        if user.verify_password(user_pwd):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')



