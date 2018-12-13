# services/users/project/config.py


import os  # new


class BaseConfig:
    """Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_ENABLED = False              # new
    DEBUG_TB_INTERCEPT_REDIRECTS = False  # new
    BCRYPT_LOG_ROUNDS = 13  # new
    SECRET_KEY = os.environ.get('SECRET_KEY')  # new
    TOKEN_EXPIRATION_DAYS = 30    # new
    TOKEN_EXPIRATION_SECONDS = 0  # new


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG_TB_ENABLED = True  # new
    BCRYPT_LOG_ROUNDS = 4  # new
    


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')
    BCRYPT_LOG_ROUNDS = 4  # new
    TOKEN_EXPIRATION_DAYS = 0     # new
    TOKEN_EXPIRATION_SECONDS = 3  # new


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False  # new
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
