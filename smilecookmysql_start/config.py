class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:password@127.0.0.1:3306/smilecook_class'
    SQLALCHEMY_TRACK_MODIFICATIONS = False