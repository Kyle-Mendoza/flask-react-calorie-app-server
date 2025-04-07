from flask import request, jsonify
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
      user_identity = get_jwt_identity()
    except ExpiredSignatureError:
      return jsonify({"message": "Token has expired!"}), 401
    except DecodeError:
      return jsonify({"message": "Token is invalid!"}), 401
    except Exception as e:
      return jsonify({"message": "Token is missing or invalid!"}), 401


    # Attach the user identity to the request object
    request.user_identity = user_identity
    return func(*args, **kwargs)

  return wrapper
