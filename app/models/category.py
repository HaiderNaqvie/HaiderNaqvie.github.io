from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from slugify import slugify

from app.extensions import db


class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(300))

    posts = relationship("Post", back_populates="category")

    def ensure_slug(self) -> None:
        if not self.slug:
            self.slug = slugify(self.name)[:120]
