
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import configs
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config.from_object(configs['development'])
    db.init_app(app)
    from .routes import api
    app.register_blueprint(api)
    return app
from .models import Movies
