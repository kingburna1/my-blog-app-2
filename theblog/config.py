import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    
    # Manually build the URI to ensure no 'None' values slip in
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST', 'localhost') 
    port = os.environ.get('DB_PORT', '3307')      
    db_name = os.environ.get('DB_NAME')

    SQLALCHEMY_DATABASE_URI = f"mysql://{user}:{password}@{host}:{port}/{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False