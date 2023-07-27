from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from dotenv import load_dotenv
import os
from os import path

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
database = os.getenv('DB_NAME')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database}'

db = SQLAlchemy(app)

from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix= '/')
app.register_blueprint(auth, url_prefix='/')

from .models import User, Task

login_manager = LoginManager()
login_manager.login_view = 'views.index'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

with app.app_context():
    db.create_all()
    print('Database created !')