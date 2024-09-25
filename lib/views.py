#   Import responsories
from lib.modal import GithubApi
from flask.views import MethodView
from flask import render_template, request, flash

class Index(MethodView):

    #   Initialize methods and database
    methods = ["GET", "POST"]

    def __init__(self) -> None:
        super().__init__()

    def get(self):

        #   Initialize database
        GithubApi().updateDatabase('fkh-ps.db', 'git_pro')


        #   For every first call this function
        #   Database calls
        return render_template("index.html", portefolio = self.initialize_database())

    def post(self): pass


    def initialize_database(self):
            
            GithubApi().updateDatabase('fkh-ps.db', 'git_pro')

            return GithubApi().updateDatabase('fkh-ps.db', 'git_pro')

