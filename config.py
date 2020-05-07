import os

class Config:
    
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'postgres://dhtumlkriiojhv:659169ad1a2ce6c3895cdd695088ab8189eabd95353f84fb14ed6088723ea41c@ec2-52-202-146-43.compute-1.amazonaws.com:5432/dgsb76aacv5u8'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")       

    SIMPLEMDE_JS_IIFE=True
    SIMPLEMDE_USE_CDN=True
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}