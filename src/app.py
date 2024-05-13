import os

from flask import Flask, send_from_directory

from src.controllers.controller import IndexController, DeletePacienteController, UpdatePacienteController, \
    CreatePacienteController, GetPacienteController
from src.db import session
from src.model.Paciente import Paciente

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'development'
)

rotasConfiguradas = {
    "index_route": "/", "index_controller": IndexController.as_view("index"),
    "delete_route": "/delete/paciente/<int:code>", "delete_controller": DeletePacienteController.as_view("delete"),
    "update_route": "/update/paciente/<int:code>", "update_controller": UpdatePacienteController.as_view("update"),
    "createcoleta_route": "/paciente/create/", "createcoleta_controller": CreatePacienteController.as_view("post"),
    "get_paciente_route": "/get/paciente/", "get_paciente_controller": GetPacienteController.as_view("get"),
   # "get_paciente_by_id_route": "/get/paciente/<int:code>", "get_paciente_by_id_controller": GetPacienteController.as_view("get_by_id"),
}

app.add_url_rule(rotasConfiguradas["index_route"], view_func=rotasConfiguradas["index_controller"])
app.add_url_rule(rotasConfiguradas["delete_route"], view_func=rotasConfiguradas["delete_controller"])
app.add_url_rule(rotasConfiguradas["update_route"], view_func=rotasConfiguradas["update_controller"])
app.add_url_rule(rotasConfiguradas["get_paciente_route"], view_func=rotasConfiguradas["get_paciente_controller"])
#app.add_url_rule(rotasConfiguradas["get_paciente_by_id_route"], view_func=rotasConfiguradas["get_paciente_by_id_controller"])
app.add_url_rule(rotasConfiguradas["createcoleta_route"], view_func=rotasConfiguradas["createcoleta_controller"])


@app.route("/<path:unknown>")
def not_found(unknown):
    return "ERROR 404" + unknown, 404


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'images/fav-icon/favicon.ico', mimetype='image/x-icon')
