from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from theblog.config import Config 
from flask_mail import Mail
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
bcrypt = Bcrypt() 
csrf = CSRFProtect()




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class) 
    migrate.init_app(app, db)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    
    
    from theblog import  models
    from theblog.main.routes import main
    from theblog.errors.handlers import errors
    from theblog.users.routes import users
    from theblog.post.routes import posts
    
    app.register_blueprint(users)
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(posts)

    return app
