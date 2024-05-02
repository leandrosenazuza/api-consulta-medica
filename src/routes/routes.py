from src.controllers.controller import *
from src.controllers.errors import NotFoundController

routes = {
    "intex_route": "/", "index_controller": IndexController.as_view("index"),
}



