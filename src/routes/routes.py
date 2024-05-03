from src.controllers.controller import *
from src.controllers.errors import NotFoundController

routes = {
    "index_route": "/", "index_controller": IndexController.as_view("index"),
}



