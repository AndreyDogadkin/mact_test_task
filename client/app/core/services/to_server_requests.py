from http import HTTPStatus

import requests
from pydantic import ValidationError

from app.base.exceptions import ForUserException
from app.base.helpers import get_local_date_and_time
from app.config import config
from app.response_schemas.response_text_count import (
    TextAndCountSchema,
    TextAndCountListSchema,
)


class ToServerRequests:
    """Взаимодействие с сервером."""

    CONFIG = config

    @staticmethod
    def __validate_response(response_data, schema, is_list=False):
        """Валидация ответа."""
        try:
            if is_list:
                valid_data = schema(data=response_data.json())
            else:
                valid_data = schema(**response_data.json())
            return valid_data
        except ValidationError:
            raise ForUserException("Ошибка валидации ответа.")

    @classmethod
    def get_counters(cls) -> tuple[TextAndCountListSchema | None, int]:
        """Запрос на получение всех объектов."""
        response = requests.get(config.counters_url)
        status_code = response.status_code
        if status_code != HTTPStatus.OK:
            return None, status_code
        valid_data = cls.__validate_response(
            response_data=response,
            schema=TextAndCountListSchema,
            is_list=True,
        )
        return valid_data, status_code

    @classmethod
    def post_counter(cls, **kwargs) -> tuple[TextAndCountSchema | None, int]:
        """Запрос на добавление объекта."""
        kwargs["local_date"], kwargs["local_time"] = get_local_date_and_time()
        response = requests.post(url=config.counters_url, json=kwargs)
        status_code = response.status_code
        if status_code != HTTPStatus.CREATED:
            return None, status_code
        valid_data = cls.__validate_response(
            response_data=response,
            schema=TextAndCountSchema,
        )
        return valid_data, status_code
