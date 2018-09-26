from functools import wraps
from flask import request,session

def auth(func):
    @wraps(func)
    def decorated_func(*args,**kwargs):
        if 'id' in session:
            return func(*args,**kwargs)
        return "<h1>Dude you not logged in go and make yo momma proud</h1>"
    return decorated_func
    