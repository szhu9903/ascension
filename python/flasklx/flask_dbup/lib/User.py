
from flask_login import UserMixin
from helper.db_helper import *
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin):
    def __init__(self,id):
        self.id = id
        self.username = None
        self.user_data = None


    # 校验密码
    def verify_password(self,password):
        password_hash = self.get_password_hash()
        if password_hash:
           return check_password_hash(password_hash,password)
        return False


    def get_password_hash(self):
        pwd_sql = "select zpwd from zsj_blog_user where  zid='%s'"%self.id
        try:
            user_pwd = getSelect(pwd_sql)
            if user_pwd:
                return user_pwd[0][0]
        except:
            return None
        return None

    @staticmethod
    def get_username(username):
        get_userid = "select zid from zsj_blog_user where zaccount='%s'"%username
        try:
            user_id = getSelect(get_userid)
            if user_id:
                return user_id[0][0]
        except:
            return None
        return None

    @staticmethod
    def get(user_id):
        if not user_id:
            return None
        get_user_sql = "select zid,zaccount,zsex from zsj_blog_user where zid='%s'"%user_id
        try:
            user_data = getSelect(get_user_sql)
            if user_data:
                user = User(user_id)
                user.user_data = user_data
                user.username = user_data[0][1]
                return user
        except:
            return None
        return None




