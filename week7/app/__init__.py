from flask import Flask 
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # initialize our database object and construct it with our app
migrate = Migrate(app, db) # initialize our migration function so that we can make changes and construct it with our database

from app import routes, models
