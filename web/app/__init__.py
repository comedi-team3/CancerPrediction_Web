# app initialize

from flask import Flask, url_for
from importlib import import_module
from app.main import blueprint
from flask_mysqldb import MySQL

app=Flask(__name__)

# 2번 라인에서 추가한 파일 연동해줌
def register_blueprints(app):
    for module_name in ('base', 'main'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def create_db():
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'comedi'
    app.config['MYSQL_DB'] = 'comedi'


def create_app():
    app=Flask(__name__, static_folder='base/static')
    create_db()
    #app.config.from_pyfile('config.py')
   # mysql = MySQL(app)
    register_blueprints(app)
    return app