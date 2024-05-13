import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY', 'development'),
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{os.environ.get('DB_USER', 'root')}:{os.environ.get('DB_PASS', 'root')}@{os.environ.get('DB_HOST', '127.0.0.1')}:{os.environ.get('DB_PORT', '3306')}/{os.environ.get('DB_NAME', 'mysql')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

Base = declarative_base()

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], pool_recycle=3600, echo=True)
conn = engine.connect()
