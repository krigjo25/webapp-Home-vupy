import os
from dotenv import load_dotenv

from lib.model import GithubApi
from flask.views import MethodView
from flask import render_template, request, flash

from lib.model import SQL

#   Load environment variables
load_dotenv()

class Index(MethodView):

    #   Initialize methods and database
    methods = ["GET", "POST"]

    def __init__(self) -> None:
        super().__init__()

    def get(self): 
        
        return render_template("index.html", portefolio =False ) # GithubApi().fetch_repos())

    def post(self): 

        #   Handle post request
        req = request.form
        return 

