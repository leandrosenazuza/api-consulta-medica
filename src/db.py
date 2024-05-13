import os


from flask import Flask, send_from_directory
from src.routes.routes import routes


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY', 'development'),
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{os.environ.get('DB_USER', 'root')}:{os.environ.get('DB_PASS', 'root')}@{os.environ.get('DB_HOST', '127.0.0.1')}:{os.environ.get('DB_PORT', '3306')}/{os.environ.get('DB_NAME', 'mysql')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)



# Define suas rotas
app.add_url_rule(routes["index_route"], view_func=routes["index_controller"])
app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])
app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])
app.add_url_rule(routes["get_paciente_route"], view_func=routes["get_paciente_controller"])
app.add_url_rule(routes["createcoleta_route"], view_func=routes["createcoleta_controller"])

@app.route("/<path:unknown>")
def not_found(unknown):
    return "ERROR 404" + unknown, 404

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'images/fav-icon/favicon.ico', mimetype='image/x-icon')

