#   Index page
#   Importing libraries
import asyncio
import datetime as dt

from dotenv import load_dotenv
from lib.model import GithubApi
from flask.views import MethodView
from flask import render_template, flash

#   Load environment variables
load_dotenv()

class Index(MethodView):

    #   Initialize methods and database
    methods = ["GET", "POST"]
    repo = None
    Dailylog = None
    WorkoutLog = None

    def __init__(self) -> None:
        super().__init__()
        
    async def get(self): 
        return render_template("index.html", portefolio = self.repo, links = { "mailbox": "mailto:krigjo25@outlook.com", "linkedin": "https://www.linkedin.com/in/krigjo25", "github": "https://www.github.com/krigjo25"})

    def post(self): 

        #   Handle post request
        return render_template("index.html")

    def SendFlash(self):

        now = dt.datetime.now()

        match (now):
            
            case _ if now.month == 12 and now.day == 24:
                flash("🎅 Merry Christmas 🎅")
            
            case _ if now.month == 2 and now.day == 25:
                flash("🎂 Happy Birthday @krigjo25 🎁")

            case _ if now.month == 2 and now.day == 14:
                flash("💖 Happy Valentines Day 💖")
                
            case _ if now.month == 10 and now.day == 31 or now.month == 11 and now.day == 1:
                flash("👻 Happy Halloween 👻")

            case _ if now.month == 1 and now.day < 10 or now.month == 12 and now.day == 30:
                flash("🎉 Happy New Year 🎉")
            
            case _ if now.month == 5 and now.day == 17:
                flash("🇳🇴 Happy Independence Day Norway 🇳🇴")
            case _ :
                flash("Certified Specializations")

    async def UpdateRepo(self):
        Index.repo = await GithubApi().fetch_repos()
    
    async def UpdateWorkout(self):
        pass

    async def DailyLog(self):
        pass

    async def Tasks(self):
        
        #   Send flash messages
        self.SendFlash()

        #   Wait for the tasks to complete
        await self.UpdateRepo()






    
