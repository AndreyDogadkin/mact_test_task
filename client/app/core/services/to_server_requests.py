from http import HTTPStatus

import requests

from app.base.helpers import get_local_date_and_time
from app.config import config


class ToServerRequests:
    """Взаимодействие с сервером."""

    CONFIG = config

    @classmethod
    def get_counters(cls) -> tuple[str | None, int]:
        """Запрос на получение всех объектов."""
        response = requests.get(config.counters_url)
        status_code = response.status_code
        if status_code == HTTPStatus.OK:
            return response.text, response.status_code
        return None, status_code

    @classmethod
    def post_counter(cls, **kwargs) -> tuple[str | None, int]:
        """Запрос на добавление объекта."""
        kwargs["local_date"], kwargs["local_time"] = get_local_date_and_time()
        response = requests.post(url=config.counters_url, json=kwargs)
        status_code = response.status_code
        if status_code == HTTPStatus.CREATED:
            return response.text, status_code
        return None, status_code
