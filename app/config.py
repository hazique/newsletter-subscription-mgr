class Config:
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'jdbc:h2:mem:testdb'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/test_db'

