from pathlib import Path

APP_DIR = Path(__name__).resolve().parent


class AppConfig(object):
    SQLALCHEMY_DATABASE_URI: str = f"sqlite:///{APP_DIR / 'app.db'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
