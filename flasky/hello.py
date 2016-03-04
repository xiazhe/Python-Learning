# manage.py
from flask import Flask
from flask.ext.script import Manager, Command


app = Flask(__name__)
manager = Manager(app)
@manager.command
def hello():
    print "hello"

if __name__ == "__main__":
    manager.run()