import os
import secrets

from dotenv import load_dotenv

load_dotenv()

class Config:

  # General application settings
  FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", secrets.token_hex(24))
  JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", secrets.token_hex(32))

  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")


class DevelopmentConfig(Config):
  DEBUG=True
  ENV='development'

class TestingConfig(Config):
  pass


class StagingConfig(Config):
  pass

class ProductionConfig(Config):
  pass
