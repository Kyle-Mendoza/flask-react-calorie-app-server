
import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from app.extensions import db, migrate
from app.routes.user.user_routes import main
from app.routes.admin.admin_routes import admin
from app.routes.admin.food_routes import food

from app.scripts.seed import seed
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig

load_dotenv()

def create_app():
  app = Flask(__name__)

  app.cli.add_command(seed)

  env = os.getenv("FLASK_ENV", "development")

  if env == "development":
    app.config.from_object(DevelopmentConfig)
  elif env == "testing":
    app.config.from_object(TestingConfig)
  elif env == "production":
    app.config.from_object(ProductionConfig)


  db.init_app(app)
  migrate.init_app(app, db)
  jwt = JWTManager(app)

  with app.app_context():
    from app.models.user import User  # Ensure User model is imported
    from app.models.admin import Admin  # Ensure Admin model is imported
    from app.models.food import Food

  CORS(app)

  app.register_blueprint(main)

  app.register_blueprint(admin, url_prefix="/api/admin")
  app.register_blueprint(food, url_prefix="/api/admin/food")


  return app
