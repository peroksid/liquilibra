from flask import Flask

# define normal python package to import from .
from liquilibra import request_api
from liquilibra import db

app = Flask(__name__)

app.register_blueprint(request_api.bp)
app.config.from_object('liquilibra.default_settings')
app.config.from_envvar('LIQUILIBRA_SETTINGS')

db.init_app(app)