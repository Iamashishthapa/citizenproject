from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from mainfolder.config import Config

db = SQLAlchemy()

#mainapp
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #importingblueprint
    from mainfolder.main.routes import main
    from mainfolder.register.routes import register
    from mainfolder.login.routes import login
    from mainfolder.welcome.routes import welcome

    # registeringblueprint
    app.register_blueprint(main)
    app.register_blueprint(register)
    app.register_blueprint(welcome)
    app.register_blueprint(login)


    return app