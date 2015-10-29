# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = '\x9c\xa8\xe7\x93\x9c\xe5\x8d\xa1@\xe6\x9c\xa8\xe7\x93'

    # db config
    SQLALCHEMY_DATABASE_URI = \
        ('mysql://card:papaya123@card-db-test.ctjngzynjvx4.rds.cn-north-1.'
         'amazonaws.com.cn/lsj')
    SQLALCHEMY_ECHO = False

    # cache config
    CACHE_TYPE = 'memcached'
    CACHE_DEFAULT_TIMEOUT = 1800  # 默认缓存30s
    CACHE_KEY_PREFIX = 'card_'  # 所有key之前添加前缀
    CACHE_MEMCACHED_SERVERS = \
        ['card-test-mc.qpid9r.cfg.cnn1.cache.amazonaws.com.cn:11211']


class DevelopmentConfig(object):
    Debug = True
    DATABASE_URI = ''


class ProductionConfig(object):
    Debug = True
    DATABASE_URI = ''
