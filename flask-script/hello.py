# -*- coding: utf-8 -*
# manage.py
from flask import Flask
from flask.ext.script import Manager, Command

app = Flask(__name__)

manager = Manager(app)

# @command修饰符
# @manager.command
# def hello():
#     'Just say hello.'
#     print "hello"

# Command 子类
# class hello(Command):
#     "prints hello world"
#
#     def run(self):
#         print "hello world"
#
# manager.add_command('hello', hello())

# @option修饰符适用于更精细的命令行控制
# example
# python manage.py hello -n Joe -u reddit.com
@manager.option('-n', '--name', dest='name', default='joe')
@manager.option('-u', '--url', dest='url', default=None)
def hello(name, url):
    if url is None:
        print "hello", name
    else:
        print "hello", name, "from", url


# 项目中常用写法
# from app import app
# from app.models import db
#
# manager = Manager(app)
#
# @manager.command
# def dropdb():
#     if prompt_bool(
#         "Are you sure you want to lose all your data"):
#         db.drop_all()


if __name__ == "__main__":
    manager.run()