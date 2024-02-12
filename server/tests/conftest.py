import datetime
import os

import pytest

from app import app as flask_app, db
from app.models.text_and_count import TextAndCount


@pytest.fixture(scope="session")
def app():
    flask_app.config.update({"TESTING": True})
    with flask_app.app_context():
        db.create_all()
    yield flask_app


@pytest.fixture
def app_with_data(app):
    post = TextAndCount()
    post.text = "Testing text"
    post.counter = 1
    post.local_date = datetime.datetime.now().date()
    post.local_time = datetime.datetime.now().time()
    with app.app_context():
        db.session.add(post)
        db.session.commit()
    yield app
    with app.app_context():
        db.session.delete(post)
        db.session.commit()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True, scope="session")
def cleanup(request):
    yield
    os.remove("app.db.sqlite3")
