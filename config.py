import redis


class Config(object):
    # DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@localhost:3306/infomation"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    SECRET_KEY = "ffadfdsfs"
    SESSION_TYPE = 'redis'
    redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = 86400 * 2


class DevelopDebug(Config):
    DEBUG = True


class ProdutionDebug(Config):
    DEBUG = False


config_map = {"develop": DevelopDebug,
              "prodution": ProdutionDebug
              }
