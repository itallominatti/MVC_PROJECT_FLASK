from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import DBConnectionHandler

db_connection_handler = DBConnectionHandler()

app = Flask(__name__)
CORS(app)


