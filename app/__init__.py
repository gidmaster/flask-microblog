from flask import Flask
# Import site configuration
from config import Config
# Import ORM SQLAlchemy tools/frameworks
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import the Login Manager
from flask_login import LoginManager

app = Flask(__name__)
# Add config file
app.config.from_object(Config)
# Create DB
db = SQLAlchemy(app)
# Apply existing migrations
migrate = Migrate(app, db)
# Add the login manager
login = LoginManager(app)
# Automatic redirect for anomymous users
login.login_view = 'login'

from app import routes, models