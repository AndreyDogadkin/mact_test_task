from sqlalchemy import select

from app import db
from app.models.text_and_count import TextAndCount


def get_last_text_and_count():
    """Получить последний добавленный объект."""
    last_post = db.session.execute(
        select(TextAndCount).order_by(-TextAndCount.id)
    ).first()
    return last_post


def add_text_and_count(text, counter):
    """Добавить объект."""
    text_and_count = TextAndCount(text=text, counter=counter)
    with db.session() as s:
        s.add(text_and_count)
        s.commit()
    return get_last_text_and_count()


def get_text_and_cunt():
    """Получить все объекты."""
    query = select(TextAndCount)
    with db.session() as s:
        texts_and_counts = s.execute(query)
        return texts_and_counts.scalars().all()
