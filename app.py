#  Application entry point

#   Importing required depenedencies
from flask import Flask
from flask_cors import CORS
from flask_session import Session

#   Custom dependencies
from lib.views import Index
from lib.APIS.Photos import PhotoLibrary
from lib.utility.logger import AppWatcher
from lib.config import DevelopmentConfig, ProdConfig

# Initialize the logger
logger = AppWatcher()
logger.FileHandler()

#   Initialize Flask app and Extensions
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config.from_object(DevelopmentConfig)
Session(app)

CORS(app, resources={r"/*": {"origins": f"*"}})
logger.info(f"App running on {app.config['ENV']}")

@app.after_request
async def after_request(response):
    """Ensure the responses aren't cached"""
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    response.headers['Expires'] = 0
    response.headers['Paragma'] = 'no-cache'
    
    logger.info(f"Response: {response}")
    return response

#   Endpoints
app.add_url_rule("/", view_func = Index().as_view('Index',methods = ["GET"]))
app.add_url_rule("/api/photos", view_func = PhotoLibrary().as_view('Photos', methods = ["POST"]))

#   Webworkers
logger.info(f"App WebWorkers : ")

if __name__ == "__main__":
  app.run()
