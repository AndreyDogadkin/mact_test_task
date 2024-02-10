from sqlalchemy import select

from app import db


class DBMethods:
    """Класс взаимодействия с базой данных."""

    session = db.session

    @classmethod
    def add_obj(cls, model, **kwargs):
        """Добавить объект."""
        text_and_count = model(**kwargs)
        with cls.session() as s:
            s.add(text_and_count)
            s.flush()
            s.expunge(text_and_count)
            s.commit()
        return text_and_count

    @classmethod
    def get_list_objs(cls, model):
        """Получить все объекты."""
        query = select(model)
        with cls.session() as s:
            texts_and_counts = s.execute(query)
            return texts_and_counts.scalars().all()
