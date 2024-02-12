from pydantic import BaseModel


class TextAndCountSchema(BaseModel):
    id: int
    counter: int
    text: str
    local_date: str
    local_time: str
    date_time_added_utc: str


class TextAndCountListSchema(BaseModel):
    data: list[TextAndCountSchema]
