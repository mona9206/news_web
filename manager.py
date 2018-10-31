from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import create_map


# class Config(object):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@localhost:3306/infomation"
#     SQLALCHEMY_TRACK_MODIFICATIONS = Flask
#     # SQLALCHEMY_ECHO = True
#     REDIS_HOST = "127.0.0.1"
#     REDIS_PORT = 6379
#     SECRET_KEY = "ffadfdsfs"
#     SESSION_TYPE = 'redis'
#     redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
#     SESSION_USE_SIGNER = True
#     SESSION_PERMANENT = 86400 * 2


app,db = create_map("develop")
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# redis_store = redis.StrictRedis(host="127.0.0.1", port=6379)
# CSRFProtect(app)
# Session(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


# @app.route("/")
# def index():
#     return "index000"


if __name__ == '__main__':
    manager.run()
