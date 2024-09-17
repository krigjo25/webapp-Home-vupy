#   Import responsories
from modal import SQL, Github
from flask.views import MethodView
from flask import render_template, request, flash

class Index(MethodView):

    #   Initialize methods and database
    methods = ["GET", "POST"]

    def __init__(self) -> None:
        super().__init__()

    def initialize_database(self):

        return

    def get(self):

        #   Database calls
        return render_template(name = "index.html", portefolio = self.initialize_database())

    def post(self): pass

