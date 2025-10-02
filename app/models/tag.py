from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from slugify import slugify

from app.extensions import db


class Tag(db.Model):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True, nullable=False)

    posts = relationship("Post", secondary="post_tags", back_populates="tags")

    def ensure_slug(self) -> None:
        if not self.slug:
            self.slug = slugify(self.name)[:120]
