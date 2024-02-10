from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class BaseModel(DeclarativeBase):
    """Абстрактный базовый класс для моделей."""

    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    date_added: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow(),
    )
