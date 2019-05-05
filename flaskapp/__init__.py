from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
#login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from flaskapp.main.routes import main
# from flaskapp.users.routes import users
# from flaskapp.posts.routes import posts

from flaskapp.errors.handlers import errors

def create_app():
    app = Flask(__name__)
    #app.config from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.config['SECRET_KEY']=''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'

    app.register_blueprint(main)
    # app.register_blueprint(users)
    # app.register_blueprint(posts)
    
    app.register_blueprint(errors)

    return app
