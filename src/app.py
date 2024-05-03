from flask import Flask
from src.routes.routes import routes


app = Flask(__name__)

app.add_url_rule(routes["index_route"], view_func=routes["index_controller"])
app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])
app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])

@app.route("/<path:unknown>")
def not_found(unknown):
    return "ERROR 404" + unknown, 404