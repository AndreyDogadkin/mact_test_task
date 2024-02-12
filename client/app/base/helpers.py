from datetime import datetime
from http import HTTPStatus

from PyQt6.QtGui import QStandardItemModel, QStandardItem

from app.response_schemas.response_text_count import (
    TextAndCountListSchema,
    TextAndCountSchema,
)


def format_response(response_data):
    """Отформатировать ответ для в шаблон для вывода."""
    row = (
        f"Идентификатор: {response_data.id}\n"
        f"Текст: {response_data.text}\n"
        f"Нажатий за сессию: {response_data.counter}\n"
        f"Локальная дата: {response_data.local_date}\n"
        f"Локальное время: {response_data.local_time}\n"
        f"Дата добавления в БД UTC: {response_data.date_time_added_utc}\n"
    )
    return row


def response_to_list_view(
        response: tuple[
            TextAndCountListSchema | TextAndCountSchema | None, int],
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
    elif isinstance(response, TextAndCountSchema):
        q_model.appendRow(QStandardItem(f"Статус ответа: {status_code}.\n"))
        row = format_response(response)
        q_model.appendRow(QStandardItem(row))
    elif isinstance(response, TextAndCountListSchema):
        q_model.appendRow(QStandardItem(f"Статус ответа: {status_code}.\n"))
        for item in response.data:
            row = format_response(item)
            q_model.appendRow(QStandardItem(row))


def get_local_date_and_time():
    """Получить локальные дату и время."""
    now = datetime.now()
    return str(now.date()), str(now.time())
