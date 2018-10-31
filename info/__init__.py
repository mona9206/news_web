from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from config import Config,DevelopDebug,ProdutionDebug,config_map
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf import CSRFProtect
from flask_session import Session


def create_map(config_name):
    app = Flask(__name__)
    name = config_map.get(config_name)
    app.config.from_object(name)

    db = SQLAlchemy(app)
    redis_store = redis.StrictRedis(host="127.0.0.1", port=6379)
    CSRFProtect(app)
    Session(app)
    manager = Manager(app)

    Migrate(app, db)
    manager.add_command('db', MigrateCommand)

    from info.index import index_blue
    app.register_blueprint(index_blue)

    return app, db