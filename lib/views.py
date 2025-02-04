#   Index page

#   Importing libraries
import asyncio, os, datetime as dt
from dotenv import load_dotenv
from flask.views import MethodView
from lib.APIS.github import GithubAPI
from flask import render_template, flash, jsonify

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
            
            Index.repo = await GithubAPI().FetchApiJson(f"{os.getenv('GithubRepos')}")
            await asyncio.sleep(386400)
            
    async def get(self): 
        
        # Calculations
        
        await self.IndexPage()

        response = {
            'mailbox': "mailto:krigjo25@outlook.com",
            "linkedin": "https://www.linkedin.com/in/krigjo25",
            "github": "https://www.github.com/krigjo25",
            'repo': f"{Index.repo if Index.repo is not None else None}"
        }
        return jsonify(response)
    
    def post(self): 

        #   Handle post request
        
        return


    async def IndexPage(self):
        
        # Ensure that the repo is None
        if Index.repo is None:
            Index.repo = await GithubAPI().FetchApiJson(f"{os.getenv('GithubRepos')}")
            
        self.SendFlash()

        return
    
    def SendFlash(self):

        now = dt.datetime.now()

        match (now):
            
            case _ if now.month == 12 and now.day > 10 and now.day < 25:
                flash("🎅 Merry Christmas 🎅")
            
            case _ if now.month == 2 and now.day == 25:
                flash("🎂 Happy Birthday @krigjo25 🎁")

            case _ if now.month == 2 and now.day > 9 and now.day < 15:
                flash("💖 Happy Valentines Day 💖")
                
            case _ if now.month == 10 and now.day > 20 and now.month == 11 and now.day < 1:
                flash("👻 Happy Halloween 👻")

            case _ if now.month == 1 and now.day < 10 and now.month == 12 and now.day == 30:
                flash("🎉 Happy New Year 🎉")
            
            case _ if now.month == 5 and now.day < 18 and now.month == 5 and now.day > 9:
                flash("🇳🇴 Happy Independence Day Norway 🇳🇴")
            case _ :
                flash("Certified Specializations")
        return
