import os

class Config:
    
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'postgres://urbtjpbhixtzbe:cbf45bc86507a584c7e3eddf88c873baade0f16035c58555ccadd0a4b11ccd77@ec2-52-207-25-133.compute-1.amazonaws.com:5432/d959785rnkrn7i'
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