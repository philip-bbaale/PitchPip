from flask import Flask,Blueprint
main = Blueprint('main',__name__)
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_simplemde import SimpleMDE
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_uploads import UploadSet,configure_uploads,IMAGES
import os
from dotenv import load_dotenv
from flask_mail import Mail
from config import config_options


load_dotenv()
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

bootstrap = Bootstrap()
simple=SimpleMDE()
db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
photos = UploadSet('photos',IMAGES)


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
login_manager.session_protection = 'strong'


def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    simple.init_app(app)

    # Registration  blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #authentication blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    # configure UploadSet
    configure_uploads(app,photos)

    return app

