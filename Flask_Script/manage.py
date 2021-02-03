#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, prompt_bool, Shell, Server

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
manager = Manager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

@manager.command
def initdb():
    db.create_all()
    print('create db success!')

@manager.command
def dropdb():
    if prompt_bool("are you sure drop all table?"):
        db.drop_all()

@manager.option('-u','--username', dest='username', help='Your name',
                default='youzi')
@manager.option('-e','--email', dest='email', help='Your email',
                default='test@qq.com')

# 命令参数既可以用-n，也可以用--username;
# dest表示以此作为方法的入参
def insert(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    print('insert onerow success!')

# 以上通过装饰器添加命令，还可以直接通过 add_command 添加命令
def make_shell_context():
    return {'db':db, 'app':app, 'User':User}

# 进入交互模式
manager.add_command('shell', Shell(make_context=make_shell_context))
# 通过命令启动服务
manager.add_command('runserver', Server(host='127.0.0.1', port=800,
                                        use_debugger=True, use_reloader=True))



if __name__ == '__main__':
    manager.run()

'''
创建表
>python manage.py initdb
删除表
>python manage.py dropdb
增加一条数据
python manage.py insert -u youzi -e youzi@qq.com
进入交互模式
>python manage.py shell
通过命令启动服务
>python manage.py runserver
'''













