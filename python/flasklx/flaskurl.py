from flask import Flask,request,Response,make_response
# from flask_sqlalchemy import SQLAlchemy


#SQL抽象层：如果只需要数据库系统和SQL抽象层，只需要引擎部分
from sqlalchemy import create_engine,MetaData
engine = create_engine('数据库连接')
metadata = MetaData(bind=engine)




app = Flask(__name__)
# app.config['SECRET_KEY'] = 'zhu'
# app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:1017@localhost:3306/mysite_db'
# 设置这一项是每次请求结束后都会自动提交数据库中的变动
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# #实例化
# db = SQLAlchemy(app)

# @app.route('/hello',methods = ['GET','POST'])
# def Hello():
#     if request.method == 'POST':
#         return 'POST'
#     else:
#         return 'GET' 

#错误处理
class Error(Exception):
    status_code = 400
    def __init__(self,message,status_code = 400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

@app.errorhandler(Error)
def error(error):
    response = make_response(error.message)
    response.status_code = error.status_code
    return response



if __name__ == '__main__':
    app.run(debug=True)







