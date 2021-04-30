from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__) #creates flask app name
    
    #DB config
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #configures sql alchemy to give database
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development" #using postgres and how to log in to everything it son my local host computer and i am goin gto use the hello books database
     
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models.book import Book #imprt models (data objects) here
    
    from.routes import hello_world_bp #import routes here
    app.register_blueprint(hello_world_bp) #import routes (blueprints) here

    
    
    #add endpoints
    
    return app