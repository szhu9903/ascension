from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField,PasswordField,BooleanField

class LoginForm(FlaskForm):
    user_name = StringField('用户名',validators=[DataRequired()])
    user_pwd = PasswordField('密码',validators=[DataRequired()])
    remember_me = BooleanField('记住密码',default=False)



