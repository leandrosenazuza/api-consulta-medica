from src.app import app
from src.config.config import *

if(__name__ == '__main__'):
    app.run(HOST, PORT, DEBUG)