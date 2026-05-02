from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from theblog.config import Config 
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class) 
    migrate.init_app(app, db)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    
    
    from theblog import  models
    from theblog.main.routes import main
    app.register_blueprint(main)

    
    return app
