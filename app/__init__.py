from flask import Flask
# Import site configuration
from config import Config
# Import ORM SQLAlchemy tools/frameworks
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import the Login Manager
from flask_login import LoginManager
# Import Logging modules
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
# Import Mail Module
from flask_mail import Mail
# Import Bootstrap Module
from flask_bootstrap import Bootstrap

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
# Add Mail module
mail = Mail(app)
# Add Bootstrap support
bootstrap = Bootstrap(app)


if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
from app import routes, models, errors