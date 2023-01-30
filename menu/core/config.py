import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

REDIS_URL = os.getenv('REDIS_URL')

SQLALCHEMY_DATABASE_TEST_URL = os.getenv(
    'SQLALCHEMY_DATABASE_TEST_URL')

REDIS_TEST_URL = os.getenv('REDIS_TEST_URL')