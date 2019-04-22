from flask import Flask
# import site configuration
from config import Config

app = Flask(__name__)
#implement configuration from config.py
app.config.from_object(Config)

from app import routes
