from functools import wraps
from flask import abort
from flask_jwt_extended import get_jwt_identity

def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        user = get_jwt_identity()

        if user != "admin":
            abort(403)

        return func(*args, **kwargs)

    return wrapper