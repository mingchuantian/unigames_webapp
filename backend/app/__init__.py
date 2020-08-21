from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager


app = Flask(__name__)

#app.config dictionary is a general-purpose place to store config variables
#The SECRET_KEY is needed for loading flask-wtf forms. 
app.config['SECRET_KEY'] = 'this should be a password but whatever'

app.config["MONGO_URI"] = "mongodb://localhost:27017/unigames_webapp_db"

mongo = PyMongo(app)
login = LoginManager(app)
login.login_view = 'login'

from app import routes