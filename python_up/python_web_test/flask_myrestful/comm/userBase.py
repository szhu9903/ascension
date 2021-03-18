
from flask_login import UserMixin
from comm import helper
from werkzeug.security import check_password_hash

class userBase(UserMixin):
    def __init__(self, id):
        self.id = id
        self.user_data = None
        self.user_name = None

    def check_pwd(self, req_userpwd):
        user_pwd = self.get_user_pwd()
        if user_pwd:
            return check_password_hash(user_pwd, req_userpwd)
        return False

    def get_user_pwd(self):
        query_user_pwd = "select zid,zpwd from zsj_blog_user where zid='%s'" % self.id
        user_pwd = helper.get_db_data(query_user_pwd)
        return user_pwd[0]['zpwd']

    @staticmethod
    def user_id(user_name):
        query_user_id = """
        select zid from zsj_blog_user where zaccount='%s' and  zpwd is not null
        """ % user_name
        user_id = helper.get_db_data(query_user_id)
        if user_id:
            return user_id[0]['zid']
        return False

    @staticmethod
    def get(user_id):
        if not user_id:
            return None
        get_user_sql = """
                select zid,zaccount,zemail,zuser_name,zuser_photo from zsj_blog_user where zid='%s'
                """ % user_id
        try:
            user_msg = helper.get_db_data(get_user_sql)
            if user_msg:
                user = userBase(user_id)
                user.user_data = user_msg[0]
                user.user_name = user_msg[0]['zaccount']
                return user
        except:
            return None
        return None
