#   Importing responsories
import os
from dotenv import load_dotenv
from flask_session import Session
from flask import Flask


#   Custom libs
from lib.config import DevelopmentConfig
from lib.modal  import SQL
from lib.views import Index


load_dotenv()
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config.from_object(DevelopmentConfig)
Session(app)


@app.after_request
def after_request(response):
    """Ensure the responses aren't cached"""
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    response.headers['Expires'] = 0
    response.headers['Paragma'] = 'no-cache'
    return response

#   Url rules
app.add_url_rule("/", view_func=Index.as_view(name="index.html"))
