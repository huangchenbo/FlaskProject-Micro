from flask import Flask, render_template, request, make_response
import JiamiChar
import time
import SQLCAOZUO


app = Flask(__name__)
nowpage = ''
cookies = ''
login = 0  # 0=未登入 1=登入成功 2=账号或密码错误 3=账号不存在

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

    if login != 1:
        return render_template('chatroom_login.html', nowpage=nowpage, login=login)
    if login == 1:
        return app.redirect('/chatroom')
    return render_template('chatroom_login.html', nowpage=nowpage, login=login)


@app.route("/chatroom_registered", methods=['POST'])
def chatroom_reg():
    pass


@app.route('/chatroom', methods=['POST', 'GET'])
def chatroom():
    nowpage = 'chatroom'
    return render_template('chatroom.html', nowpage=nowpage, login=login)


if __name__ == '__main__':
    app.run()
