from __future__ import annotations

from datetime import datetime

from app import create_app
from app.extensions import db
from app.models import Category, Post, Tag

app = create_app()


def main() -> None:
    with app.app_context():
        tech = Category(name="Technology", slug="technology"); db.session.add(tech)
        travel = Category(name="Travel", slug="travel"); db.session.add(travel)
        health = Category(name="Health", slug="health"); db.session.add(health)
        finance = Category(name="Finance", slug="finance"); db.session.add(finance)
        lifestyle = Category(name="Lifestyle", slug="lifestyle"); db.session.add(lifestyle)

        db.session.flush()

        posts = [
            Post(
                title="AI Trends to Watch in 2025",
                slug="ai-trends-to-watch-in-2025",
                excerpt="From multimodal agents to edge inference...",
                content="<p>Full content about AI trends in 2025...</p>",
                thumbnail_url="https://picsum.photos/seed/ai2025/800/500",
                status="published",
                published_at=datetime.utcnow(),
                category_id=tech.id,
                is_featured=True,
            ),
            Post(
                title="Budget Travel Guide: 10 Countries Under $50/day",
                slug="budget-travel-guide-10-countries-under-50-day",
                excerpt="Stretch your dollars further...",
                content="<p>Full content for budget travel...</p>",
                thumbnail_url="https://picsum.photos/seed/travel/800/500",
                status="published",
                published_at=datetime.utcnow(),
                category_id=travel.id,
            ),
        ]
        db.session.add_all(posts)

        for name in ["AI", "Budget", "Health", "Investing"]:
            db.session.add(Tag(name=name, slug=name.lower()))

        db.session.commit()
        print("Seeded sample categories and posts")


if __name__ == "__main__":
    main()
