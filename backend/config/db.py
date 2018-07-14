from flask_pymongo import PyMongo

def db_create(app, debug=False):
    if debug:
        app.config["MONGO_URI"] = "mongodb://localhost:27017/TremaTest"
    else:
        app.config["MONGO_URI"] = "mongodb://localhost:27017/Trema"
    
    return PyMongo(app)