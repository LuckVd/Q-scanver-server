from flask import Flask

from routes.task import task_bp

arl_app = Flask(__name__)
arl_app.config['BUNDLE_ERRORS'] = True

authorizations = {
    "ApiKeyAuth": {
        "type": "apiKey",
        "in": "header",
        "name": "Token"
    }
}


arl_app.register_blueprint(task_bp)

if __name__ == '__main__':
    arl_app.run(debug=True, port=5018, host="0.0.0.0",use_reloader=False)

