import os
import asyncio
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
    repo = None
    
    def __init__(self) -> None:
        super().__init__()

    async def update_periodically(self):
        while True:
            await asyncio.sleep(386400)
            Index.repo = await GithubApi().fetch_repos()
            
    async def get(self): 
        
        if Index.repo == None:
            Index.repo = await GithubApi().fetch_repos()

        return render_template("index.html", portefolio = self.repo)

    def post(self): 

        #   Handle post request
        req = request.form
        return render_template("index.html")

