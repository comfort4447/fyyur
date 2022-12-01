import os
from flask import Flask
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

app = Flask(__name__)
# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://abisolatayo@localhost:5432/fyyur1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False