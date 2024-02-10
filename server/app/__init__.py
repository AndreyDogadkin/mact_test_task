from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import AppConfig
from .models.base import BaseModel

db = SQLAlchemy(model_class=BaseModel)
migrate = Migrate()
marshmallow = Marshmallow()

app = Flask(__name__)
app.config.from_object(AppConfig)
db.init_app(app=app)
migrate.init_app(app=app, db=db)
marshmallow.init_app(app=app)

from .views import api_views  # noqa
from .models.text_and_count import TextAndCount  # noqa
