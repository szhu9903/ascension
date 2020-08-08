
from resource import  app,login_message
from wtf.login import LoginForm
from flask import render_template,request,redirect,url_for
from lib.user import User
from flask_login import login_user,login_required,logout_user,current_user

@login_message.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = request.form.get('user_name',None)
        user_pwd = request.form.get('user_pwd',None)
        remember_me = request.form.get('remember_me',False)
        user = User(user_name)
        #校验密码
        if user.verify_password(user_pwd):
            login_user(user,remember=remember_me)
            return redirect(request.args.get('next') or url_for('main'))
    return render_template('login.html',title='登录',form=form)

@app.route('/')
@app.route('/main')
@login_required
def main():
    current = current_user
    return render_template('main.html',user_name=current.user_name)

@app.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('login'))


