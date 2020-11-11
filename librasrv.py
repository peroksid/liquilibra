from flask import Flask

from liquilibra import request_api

app = Flask(__name__)

app.register_blueprint(request_api.bp)