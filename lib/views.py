#   Import responsories
from lib.modal import GithubApi
from flask.views import MethodView
from flask import render_template, request, flash

from lib.modal import SQL
class Index(MethodView):

    #   Initialize methods and database
    methods = ["GET", "POST"]

    def __init__(self) -> None:
        super().__init__()

    def get(self):

        #   Initialize database
        self.initialize_database()
        
        return render_template("index.html", portefolio = SQL('fkh-ps.db').select_records('git_pro', 'SELECT'))

    def post(self): pass


    def initialize_database(self):

            return GithubApi().updateDatabase('fkh-ps.db', 'git_pro')

