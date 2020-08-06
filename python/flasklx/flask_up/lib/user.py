
from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash
from resource import PROFILE_FILE
import json,uuid

class User(UserMixin):
    def __init__(self,user_name):
        self.user_name = user_name
        self.id = self.get_id()

    # 禁止读取密码
    @property
    def password(self):
        raise AttributeError('密码不是可读属性')

    @password.setter
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
        with open(PROFILE_FILE,'w+') as f:
            try:
                profile = json.loads(f)
            except ValueError:
                profile = {}
            profile[self.user_name] = [self.id,self.password_hash]
            f.write(json.dumps(profile))

    def cerify_password(self,password):
        password_hash = self.get_password_hash()
        if password_hash is None:
            return False
        return check_password_hash(self.password_hash,password)

    def get_password_hash(self):
        try:
            with open(PROFILE_FILE) as f:
                profile_user = json.loads(f)
                user_info = profile_user.get(self.user_name,None)
                if user_info is not None:
                    return user_info[1]
        except Exception:
            return None

    def get_id(self):
        if self.user_name is not None:
            try:
                with open(PROFILE_FILE) as f:
                    user_profile = json.loads(f)
                    if self.user_name in user_profile:
                        return user_profile[self.user_name][0]
            except:
                pass
        return str(uuid.uuid4())

    @staticmethod
    def get(user_id):
        if not user_id:
            return None
        try:
            with open(PROFILE_FILE) as f:
                user_profile = json.loads(f)
                for user_name,profile in user_profile.iteritems():
                    if profile[0] == user_id:
                        return User(user_name)
        except:
            return None
        return None





