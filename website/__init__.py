from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'IJKDFJMNVDO LMVMFNCVCVD'
    app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DB_NAME}' #this is to tell flask where to find the database.
    db.init_app(app) #Initiallising the database in the app.


#registering our blueprints

    from .views import views
    from .auth import  auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Note

    create_database()



    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')