from pydantic import BaseModel


class TextAndCountSchema(BaseModel):
    """Схема для валидации объекта TextAndCount."""

    id: int
    counter: int
    text: str
    local_date: str
    local_time: str
    date_time_added_utc: str


class TextAndCountListSchema(BaseModel):
    """Схема для валидации массива объектов TextAndCount."""

    data: list[TextAndCountSchema]
