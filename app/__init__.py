from flask import Flask
from flask_cors import CORS
from app.routes.main_routes import main
from app.routes.api_routes import api

def create_app():
  app = Flask(__name__)

  CORS(app)

  app.register_blueprint(main)
  app.register_blueprint(api, url_prefix="/api")

  return app
