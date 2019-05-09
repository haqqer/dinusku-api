from flask import Flask
from app import api_bp
from config import app_config


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(app_config[config_filename])
    app.config.from_pyfile('config.py')
    app.register_blueprint(api_bp)   

    return app

app = create_app('development')

if __name__ == '__main__':    
    app.run(debug=True, host="0.0.0.0", port=9000)
