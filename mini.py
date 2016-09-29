# -*- coding: utf-8 -*
# A Minimal Application http://flask-restful-cn.readthedocs.io/zh/latest/quickstart.html#api
from flask import Flask

app = Flask(__name__)


# 请求钩子
@app.before_first_request
def before_first_request():
    print 'before first request'


@app.before_request
def before_request():
    doSomeThing = 'do something'
    print 'before request' + doSomeThing


# @app.after_request
# def after_request():
#     print 'after request'
#     pass


# @app.teardown_request
# def teardown_request():
#     print 'teardown request'
#     pass

@app.route('/')
def hello_world():

    return 'Hello World!'

if __name__ == '__main__':
    app.run(port=8002, debug=True)

# socket.error: [Errno 10013]
# 更换端口
# netstat -ban
