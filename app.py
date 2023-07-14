from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import JiamiChar
import time
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flasksql?charset=utf8mb4'
app.config['SECRET_KEY'] = 'FLASKSQLANDCHAT'
db = SQLAlchemy(app)
nowpage = ''
cookies = ''
login = 0  # 0=未登入 2=账号或密码错误 3=注册成功，请登入
reg = 0  # 0=None 1=账号已存在


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    # public_id = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    # admin = db.Column(db.Boolean)
    def __init__(self, username, password):
        self.username = username
        self.password = password


with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/index')
def IndexHtml():
    nowpage = 'index'
    return render_template('index.html', nowpage=nowpage)



@app.route('/info')
def info():
    nowpage = 'info'
    return render_template('info.html', nowpage=nowpage)


@app.route('/download')
def download_page():
    nowpage = 'download'
    return render_template('Download.html', nowpage=nowpage)


@app.route('/chatroom_login', methods=['POST', 'GET'])
def chatroom_login():
    global login
    nowpage = 'chatroom'
    if request.method == "POST":
        a = request.values
        login_user = User.query.filter_by(username=a['username'], password=a['password'])
        if login_user.first() is not None:
            # 登入成功
            session['username'] = login_user[0].username
            return app.redirect('chatroom')
        else:
            return render_template('chatroom_login.html', nowpage=nowpage, login=2)
    else:
        return render_template('chatroom_login.html', nowpage=nowpage, login=login)


@app.route("/chatroom_registered", methods=['POST', 'GET'])
def chatroom_reg():
    if request.method == "POST":
        a = request.values
        reg_user = User.query.filter_by(username=a['username'])
        if reg_user.first() is not None:
            return render_template('chatroom_registered.html', reg=1)
        else:
            reg_user_mysql = User(username=a['username'], password=a['password'])
            db.session.add(reg_user_mysql)
            db.session.commit()
            return app.redirect('chatroom_login')
            # return render_template('chatroom_login.html', nowpage='chatroom', login=3)
    else:
        return render_template('chatroom_registered.html', nowpage=nowpage, reg=0)


@app.route('/chatroom', methods=['POST', 'GET'])
def chatroom():
    nowpage = 'chatroom'
    if session.get('username') is  None:
        return render_template('chatroom.html', nowpage=nowpage, login=login)
    else:
        return render_template('chatroom.html', nowpage=nowpage)


if __name__ == '__main__':
    app.run()