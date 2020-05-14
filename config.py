import os

class Config:
    
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'postgres://zsaoexvbzfajsw:37be5cef0cff25b41be4e2b5419525b299ebc7c2d8808943ca8c822e0468045f@ec2-52-202-146-43.compute-1.amazonaws.com:5432/d9j96iod7o3ela'
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