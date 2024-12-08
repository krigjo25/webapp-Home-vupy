import os
import asyncio
import datetime as dt
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

    async def UpdateRepo(self):

        while True:
            await asyncio.sleep(386400)
            Index.repo = await GithubApi().fetch_repos()
            
    async def get(self): 
        
        # Calculations

        await self.IndexPage()
        return render_template("index.html", portefolio = self.repo, links = { "mailbox": 'mailto:krigjo25@outlook.com', "linkedin": 'https://', "github": 'https://www.github.com/krigjo25'})

    def post(self): 

        #   Handle post request
        req = request.form
        return render_template("index.html")


    async def IndexPage(self):
        
        # Ensure that the repo is None
        if Index.repo is None:
            Index.repo = await GithubApi().fetch_repos()
            
        

        self.SendFlash()

        return
    
    def SendFlash(self):

        now = dt.datetime.now()

        match (now):
            
            case _ if now.month == 12 and now.day == 24:
                flash("Merry Christmas")
            
            case _ if now.month == 2 and now.day == 25:
                flash("Happy Birthday @krigjo25")

            case _ if now.month == 2 and now.day == 14:
                flash("Happy Valentines Day")
                
            case _ if now.month == 10 and now.day == 31:
                flash("Happy Halloween")
            
            case _ if now.month == 1 and now.day == 1 or now.month == 12 and now.day == 31 and now.hour == 23:
                flash("Happy New Year")
            
            case _ if now.month == 5 and now.day == 17:
                flash(f"🇳🇴 Happy Independence Day Norway 🇳🇴")
            case _ :
                flash("Certified Specializations")
        return




    
