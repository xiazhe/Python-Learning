# A Minimal Application
from flask import Flask

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    print 'before first request'

@app.before_request
def before_request():
    print 'before request'

@app.after_request
def after_request():
    print 'after request'

@app.teardown_request
def teardown_request():
    print 'teardown request'

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(port=8000)