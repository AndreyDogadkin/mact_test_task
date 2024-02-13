import pytest

from app.ui import main_window


@pytest.fixture
def app(qtbot):
    qt_app = main_window.AppMainWindow()
    qtbot.addWidget(qt_app)
    yield qt_app
    qt_app.close()
