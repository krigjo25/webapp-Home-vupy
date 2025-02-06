#   Utility tools for the application


#   Importing necsessary dependencies
import os

from lib.APIS.github import GithubAPI
from lib.APIS.heavy import HeavyAPI

class UtilityTools(object):


    def UpdateHeavy(self):
        return HeavyAPI().FetchWorkouts()

    def UpdateGithub(self):
            return GithubAPI().FetchApiJson(f"{os.getenv('GithubRepos')}")

    
    def SendMessage(self, now):

        match (now):
            
            case _ if now.month == 12 and now.day > 10 and now.day < 25:
                message ="🎅 Merry Christmas 🎅"
            
            case _ if now.month == 2 and now.day == 25:
                message ="🎂 Happy Birthday @krigjo25 🎁"

            case _ if now.month == 2 and now.day > 9 and now.day < 15:
                message ="💖 Happy Valentines Day 💖"
                
            case _ if now.month == 10 and now.day > 20 and now.month == 11 and now.day < 1:
                message ="👻 Happy Halloween 👻"

            case _ if now.month == 1 and now.day < 10 and now.month == 12 and now.day == 30:
                message ="🎉 Happy New Year 🎉"
            
            case _ if now.month == 5 and now.day < 18 and now.month == 5 and now.day > 9:
                message ="🇳🇴 Happy Independence Day Norway 🇳🇴"
            case _ :
                message ="Certified Specializations"
        
        return message
