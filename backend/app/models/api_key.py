from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import BaseDbModel
from app.mappings import FKDeveloper


class ApiKey(BaseDbModel):
    """Global API key for external service access."""

    __tablename__ = "api_key"

    # Explicit String primary key. API keys are arbitrary strings and may look
    # like a UUID; keep the column varchar so lookups never emit a `::uuid` cast
    # (which fails with "operator does not exist: character varying = uuid").
    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    name: Mapped[str]
    created_by: Mapped[FKDeveloper | None]
