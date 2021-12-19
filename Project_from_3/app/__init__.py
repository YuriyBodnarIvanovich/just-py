from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from app import view