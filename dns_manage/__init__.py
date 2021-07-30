from flask import Flask

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    
    GCP = GCloudOperation() 
    #base
    app.add_url_rule('/', 'index', index)
    return app


