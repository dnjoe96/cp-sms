from flask import Flask
import africastalking
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # this is used to allow for future expansion oof the database
from config import Config
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)

# initializing SDK
# username gotten from Africastalking dashboard
# api_key was generated from the dashboard > settings
username = 'codeplateu'
api_key = 'dbc733441e6d1f39d5e028cb976f15c9e0143e3ff93d157d1f4223207e1da63a'
africastalking.initialize(username, api_key)


# initializing service for SMS
sms = africastalking.SMS

from app import route, models
