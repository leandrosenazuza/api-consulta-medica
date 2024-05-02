from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import pymysql


class IndexController(MethodView):
    def get(self):
        return ;

class post(self):
    code = request.form['nome']
