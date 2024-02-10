from app import marshmallow
from app.models.text_and_count import TextAndCount


class TextAndCountSchema(marshmallow.SQLAlchemyAutoSchema):
    """Схема для валидации объекта."""

    class Meta:
        model = TextAndCount
