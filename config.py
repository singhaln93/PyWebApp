import os

class Config(Object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"