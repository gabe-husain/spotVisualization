from flask import Flask, Blueprint, session
from routes import Routes
from oauth2 import oauth
import os

app = Flask(__name__)

app.config.from_object("configFile.DevelopmentConfig")
app.config["SESSION_COOKIE_NAME"] = 'Spotify Sesh'
app.register_blueprint(oauth)
app.register_blueprint(Routes)

app.run()