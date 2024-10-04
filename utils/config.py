import os
from dotenv import load_dotenv


load_dotenv


def get_env_variable(key, default=None):
    return os.getenv(key, default)


API_URL = get_env_variable('API_URL')
DB_NAME = get_env_variable('DB_NAME')
DB_USER = get_env_variable('DB_USER')
DB_PASSWORD = get_env_variable('DB_PASSWORD')
DB_HOST = get_env_variable('DB_HOST')
DB_PORT = get_env_variable('DB_PORT')
