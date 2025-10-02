from __future__ import annotations

from datetime import datetime
from typing import Optional

from slugify import slugify
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.extensions import db


class PostStatus(str):
    DRAFT = "draft"
    PUBLISHED = "published"


class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    slug: Mapped[str] = mapped_column(String(220), unique=True, index=True, nullable=False)
    excerpt: Mapped[Optional[str]] = mapped_column(String(300))
    content: Mapped[str] = mapped_column(Text, nullable=False)
    thumbnail_url: Mapped[Optional[str]] = mapped_column(String(500))

    status: Mapped[str] = mapped_column(String(20), default=PostStatus.DRAFT, index=True)
    published_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category_id: Mapped[Optional[int]] = mapped_column(ForeignKey("categories.id"))
    category = relationship("Category", back_populates="posts")

    # SEO fields
    seo_title: Mapped[Optional[str]] = mapped_column(String(200))
    seo_description: Mapped[Optional[str]] = mapped_column(String(300))
    canonical_url: Mapped[Optional[str]] = mapped_column(String(500))
    og_image_url: Mapped[Optional[str]] = mapped_column(String(500))

    # Engagement
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False)
    view_count: Mapped[int] = mapped_column(Integer, default=0)

    tags = relationship("Tag", secondary="post_tags", back_populates="posts")

    def ensure_slug(self) -> None:
        if not self.slug:
            self.slug = slugify(self.title)[:220]

    def ensure_excerpt(self) -> None:
        if not self.excerpt and self.content:
            self.excerpt = (self.content[:160] + "...") if len(self.content) > 160 else self.content

    def publish(self) -> None:
        self.status = PostStatus.PUBLISHED
        if not self.published_at:
            self.published_at = datetime.utcnow()


class PostTag(db.Model):
    __tablename__ = "post_tags"
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), primary_key=True)
