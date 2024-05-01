from flask import Flask
from src.routes.routes import routes

app = Flask(__name__)

app.add_url_rule(routes["ola_route"], view_func=routes["olacontroller"])