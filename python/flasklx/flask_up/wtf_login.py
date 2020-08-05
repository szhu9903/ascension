from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '9a571858-4c78-4bc0-b6d6-8fdda031fecf'

class LoginForm(FlaskForm):
    user_name = StringField('账号',validators=[DataRequired()])
    user_pwd = PasswordField('密码',validators=[DataRequired()])
    remember_me = BooleanField('记住密码',default=False)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='登录',form=form)


if __name__ == '__main__':
    import uuid
    print(uuid.uuid4())
    app.run('0.0.0.0','8888',debug=True)