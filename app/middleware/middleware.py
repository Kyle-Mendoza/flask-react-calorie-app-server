from flask import request, jsonify, g
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from jwt.exceptions import ExpiredSignatureError, DecodeError

# JWT authentication middleware
def jwt_required_middleware(func):
  """
    Middleware to ensure JWT token is provided and valid.
  """
  @wraps(func)
  def wrapper(*args, **kwargs):
    try:
      # Verify that the JWT is present and valid
      verify_jwt_in_request()
      g.user_identity = get_jwt_identity()

    except Exception as e:
      return jsonify({"message": str(e)}), 401
    
    return func(*args, **kwargs)

  return wrapper
