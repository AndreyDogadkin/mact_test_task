from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.models.base import BaseModel
from core.config import AppConfig

db = SQLAlchemy(model_class=BaseModel)
migrate = Migrate()
marshmallow = Marshmallow()

app = Flask(__name__)
app.config.from_object(AppConfig)
db.init_app(app=app)
migrate.init_app(app=app, db=db)
marshmallow.init_app(app=app)

from . import api_views  # noqa
