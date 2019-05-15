from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zhu'
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:1017@localhost:3306/mysite_db'
#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#实例化
db = SQLAlchemy(app)

@app.route('/hello',methods = ['GET','POST'])
def Hello():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET' 

if __name__ == '__main__':
    app.run(debug=True)
