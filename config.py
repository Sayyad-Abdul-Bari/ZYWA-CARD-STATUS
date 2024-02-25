# config.py

class Config:
    # Modify the following variables according to your database setup
    DB_USER = "root"
    DB_PASSWORD = "mysql"
    DB_HOST = "localhost"
    DB_NAME = "cardstatusgemini"
    
    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False



