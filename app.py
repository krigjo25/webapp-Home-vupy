#  Application entry point

#   Importing required depenedencies
import os

from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_session import Session

#   Custom dependencies
from lib.endpoint_services.github_data import Github
from lib.utils.log_config import AppWatcher
from lib.endpoint_services.Photos import PhotoLibrary
from lib.endpoint_services.announcements import Announcements
from lib.settings.env_config import DevelopmentConfig, ProdConfig

#   Initialize Enviorment variables
load_dotenv()

# Initialize the logger
logger = AppWatcher()
logger.FileHandler()

#   Initialize Flask app and Extensions
app = Flask(__name__)

if os.getenv('ENV') == 'production':
  app.config.from_object(ProdConfig()) 
  CORS(app, resources={r"/*": {"origins": f"{app.config['DOMAIN']}"}}, supports_credentials=True)

elif os.getenv('ENV') == 'development':
  CORS(app, resources={r"/*": {"origins": f"*"}}, supports_credentials=True)
  app.config.from_object(DevelopmentConfig)

logger.info(f"App running on {app.config}")

#   Configure session to use filesystem (instead of signed cookies)
Session(app)
'''
@app.after_request
async def after_request(response):
    """Ensure the responses aren't cached"""
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    response.headers['Expires'] = 0
    response.headers['Paragma'] = 'no-cache'
    
    logger.info(f"Response: {response}")
    return response
'''
#   Endpoints
app.add_url_rule("/", view_func = Announcements().as_view('Index',methods = ["GET"]))
app.add_url_rule("/api/github", view_func = Github().as_view('Github', methods = ["GET"]))
app.add_url_rule("/api/photos", view_func = PhotoLibrary().as_view('Photos', methods = ["GET"]))

#   Webworkers
if __name__ == "__main__":
  app.run()
