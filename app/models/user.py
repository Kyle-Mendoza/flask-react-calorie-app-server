from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  username = db.Column(db.String(120), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  first_name = db.Column(db.String(60), nullable=False)
  last_name = db.Column(db.String(60), nullable=False)
  weight = db.Column(db.Float, nullable=False)
  height = db.Column(db.Float, nullable=False)
  birthdate = db.Column(db.Date, nullable=False)
  password_hash = db.Column(db.String(255), nullable=False)
  physical_activity_level = db.Column(db.Float, nullable=False)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
