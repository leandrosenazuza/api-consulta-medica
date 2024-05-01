from flask.views import MethodView

class oieContorller(MethodView):
    def get(self):
        return "oie"