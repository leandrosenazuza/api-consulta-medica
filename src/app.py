from flask import Flask
from src.routes.routes import routes


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'development'
)

app.add_url_rule(routes["index_route"], view_func=routes["index_controller"])
app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])
app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])
app.add_url_rule(routes["get_paciente_route"], view_func=routes["get_paciente_controller"])
app.add_url_rule(routes["create_paciente_route"], view_func=routes["create_paciente_controller"])

@app.route("/<path:unknown>")
def not_found(unknown):
    return "ERROR 404" + unknown, 404