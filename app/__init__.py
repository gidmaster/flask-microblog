from flask import Flask
# import site configuration
from config import Config
# import ORM SQLAlchemy tools/frameworks
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
#create DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models