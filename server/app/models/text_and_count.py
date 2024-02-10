from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column, Mapped

from app import db


class TextAndCount(db.Model):
    """Модель для текста и номера нажатия."""

    text: Mapped[str] = mapped_column()
    counter: Mapped[int] = mapped_column()
    date_added = mapped_column(DateTime)
