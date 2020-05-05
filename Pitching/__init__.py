from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from  flask_migrate import Migrate, MigrateCommand
from flask_uploads import UploadSet,configure_uploads,IMAGES


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOADED_PHOTOS_DEST'] ='Pitching/static/photos'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
https://github.com/scrupycoco/PitchPip.git

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
https://github.com/scrupycoco/PitchPip.git

photos = UploadSet('photos',IMAGES)
configure_uploads(app,photos)
https://github.com/scrupycoco/PitchPip.git


from Pitching import routes
<!!!>
