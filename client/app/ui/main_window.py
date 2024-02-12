from PyQt6.QtGui import QStandardItemModel
from PyQt6.QtWidgets import QMainWindow

from app.base.helpers import response_to_list_view
from app.base.main_ui import Ui_MainWindow
from app.core.services import ToServerRequests

to_server_requests = ToServerRequests


class AppMainWindow(QMainWindow):
    """Главное UI окно приложения."""

    def __init__(self):
        super(AppMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.post_button.clicked.connect(self.on_click_post)
        self.ui.get_push_button.clicked.connect(self.on_click_get)
        self.post_model = QStandardItemModel()
        self.get_model = QStandardItemModel()
        self.ui.post_list_view.setModel(self.post_model)
        self.ui.get_list_view.setModel(self.get_model)
        self.session_post_counter = 1

    def on_click_post(self):
        """
        Нажатие на кнопку "POST".
        - Отправить запрос на добавление объекта
        - Вывести добавленный объект.
        """
        self.post_model.clear()
        text = self.ui.post_line_edit.text()
        response = to_server_requests.post_counter(
            text=text, counter=self.session_post_counter
        )
        response_to_list_view(response, self.post_model)
        self.session_post_counter += 1
        self.ui.post_line_edit.setText("")

    def on_click_get(self):
        """
        Нажатие на кнопку "GET".
        - Отправить запрос получение всех объектов
        - Вывести все полученные объекты.
        """
        self.get_model.clear()
        response = to_server_requests.get_counters()
        response_to_list_view(response, self.get_model)
