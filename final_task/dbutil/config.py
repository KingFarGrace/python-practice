DEBUG = True

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'admin'
PASSWORD = '132546'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'webspider'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True
