from flask import Flask
from src.routes.routes import routes


app = Flask(__name__)

app.add_url_rule(routes["ola_route"], view_func=routes["index_controller"])

app.register_error_handler(routes["not_found_routes"], routes["not_found_controller"])

@app.route("/<path:unknown>")
def not_found(unknown):
    return "ERROR 404" + unknown, 404