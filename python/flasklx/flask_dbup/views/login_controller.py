from  resource import app,login_message,session
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
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    user_name = request.form.get('user_name','')
    user_pwd = request.form.get('user_pwd','')
    remember_me = request.form.get('remember_me','')
    user_id = User.get_username(user_name)
    if user_id:
        user = User(user_id)
        if user.verify_password(user_pwd):
            login_user(user,remember=remember_me)
            return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/test/insert',methods=['GET','POST'])
def test_insert():
    try:
        sql1 = """insert into zsj_blog_type(ztype_name, zblog_count)VALUES ('测试事务提交',1)"""
        session.add(sql1)
        session.commit()
    except Exception as er:
        session.rollback()
        print(er)
        return 'Error'



