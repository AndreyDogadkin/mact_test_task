from datetime import time, date

from sqlalchemy.orm import mapped_column, Mapped

from app import db


class TextAndCount(db.Model):
    """Модель для текста и номера нажатия."""

    text: Mapped[str] = mapped_column()
    counter: Mapped[int] = mapped_column()
    local_time: Mapped[time] = mapped_column()
    local_date: Mapped[date] = mapped_column()
