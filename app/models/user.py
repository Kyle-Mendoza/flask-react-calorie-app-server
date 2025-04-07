from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  username = db.Column(db.String(120), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)


  def set_password(self, password):
    pass

  def check_password(self, password):
    pass
