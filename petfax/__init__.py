import os
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)

    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return "Hello, Petfax!"

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    # register facts blueprint
    from . import facts 
    app.register_blueprint(facts.bp)

    return app

