from flask import Blueprint, render_template
from oauth2 import oauth
import os

secret_key = os.getenv('SECRET')
Routes = Blueprint("Routes", __name__)
Routes.register_blueprint(oauth)

@Routes.route('/')
@Routes.route('/index')
def index():
    return render_template("base.html")



