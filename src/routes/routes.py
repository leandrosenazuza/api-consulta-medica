from src.controllers.controller import *

routes = {
    "index_route": "/", "index_controller": IndexController.as_view("index"),
    "delete_route": "/delete/paciente/<int:code>", "delete_controller": DeletePacienteController.as_view("delete"),
    "update_route": "/update/paciente/<int:code>", "update_controller": UpdatePacienteController.as_view("update"),
    "createcoleta_route": "/paciente/create/", "createcoleta_controller": CreatePacienteController.as_view("post"),
    "get_paciente_route": "/get/paciente/", "get_paciente_controller": GetPacienteController.as_view("get"),
}



