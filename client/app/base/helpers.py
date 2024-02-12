from datetime import datetime
from http import HTTPStatus

from PyQt6.QtGui import QStandardItemModel, QStandardItem


def response_to_list_view(
        response: tuple[str | None, int],
        q_model: QStandardItemModel,
):
    """Обработка полученного ответа."""
    statuses = [HTTPStatus.OK, HTTPStatus.CREATED, HTTPStatus.BAD_REQUEST]
    response, status_code = response
    if not response or status_code not in statuses:
        q_model.appendRow(
            QStandardItem(
                f"Ошибка при выполнении запроса. Статус: {status_code}"
            ),
        )
    else:
        q_model.appendColumn(
            [
                QStandardItem(f"Статус: {status_code} \n"),
                QStandardItem(response),
            ]
        )


def get_local_date_and_time():
    """Получить локальные дату и время."""
    now = datetime.now()
    return str(now.date()), str(now.time())
