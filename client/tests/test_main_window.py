from PyQt6 import QtCore


def test_labels(app):
    assert app.ui.post_label.text() == "POST request"
    assert app.ui.get_label.text() == "GET request"


def test_buttons_text(app):
    assert app.ui.post_button.text() == "POST"
    assert app.ui.get_push_button.text() == "GET"


def test_line_edit_placeholder_text(app):
    assert app.ui.post_line_edit.placeholderText() == "Введите текст..."


def test_push_buttons_without_server(app, qtbot):
    qtbot.mouseClick(app.ui.get_push_button, QtCore.Qt.MouseButton.LeftButton)
    qtbot.mouseClick(app.ui.post_button, QtCore.Qt.MouseButton.LeftButton)
    assert app.get_model.rowCount() == 1
    assert app.post_model.rowCount() == 1
    assert (
            "Ошибка при выполнении "
            "запроса. Статус:" in app.get_model.takeRow(0)[0].text()
    )
    assert (
            "Ошибка при выполнении "
            "запроса. Статус:" in app.post_model.takeRow(0)[0].text()
    )


def test_remove_text_line_edit_after_request(app, qtbot):
    qtbot.keyClicks(app.ui.post_line_edit, "Test text")
    assert app.ui.post_line_edit.text() == "Test text"
    qtbot.mouseClick(app.ui.post_button, QtCore.Qt.MouseButton.LeftButton)
    assert app.ui.post_line_edit.text() == ""
