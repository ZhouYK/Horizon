"""AIbase (aibase.com) news scraper.

Scrapes the AIbase news list page, which publishes daily AI industry news
covering model releases, tool launches, and research highlights. The site
has no public RSS or API, so this scraper parses the HTML list page.

Date handling: the list page only shows relative timestamps ("1 days ago",
"3 hours ago", etc.). These are converted to approximate UTC datetimes
using the current time at fetch time. Items with dates older than `since`
are dropped. Because relative times have day-level granularity, items
published "1 days ago" could be up to 48 hours old; the scraper applies
a generous tolerance and lets the AI scoring step rank by quality.
"""

from __future__ import annotations

import hashlib
import logging
import re
from datetime import datetime, timedelta, timezone
from typing import List, Optional

import httpx
from bs4 import BeautifulSoup

from .base import BaseScraper
from ..models import AibaseConfig, ContentItem, SourceType

logger = logging.getLogger(__name__)

_BASE_URL = "https://www.aibase.com"
_NEWS_PATH = {"en": "/news", "zh": "/zh/news"}
_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

_RELATIVE_RE = re.compile(
    r"(\d+)\s+(second|minute|hour|day|week|month)s?\s+ago", re.IGNORECASE
)


def _parse_relative_time(text: str, now: datetime) -> Optional[datetime]:
    """Convert a relative time string to an aware UTC datetime.

    Supports: "N seconds/minutes/hours/days/weeks/months ago".
    Returns None when the text does not match.
    """
    m = _RELATIVE_RE.search(text)
    if not m:
        return None
    value = int(m.group(1))
    unit = m.group(2).lower()
    deltas = {
        "second": timedelta(seconds=value),
        "minute": timedelta(minutes=value),
        "hour": timedelta(hours=value),
        "day": timedelta(days=value),
        "week": timedelta(weeks=value),
        "month": timedelta(days=value * 30),
    }
    return now - deltas[unit]


class AibaseScraper(BaseScraper):
    """Scraper for AIbase news (aibase.com)."""

    def __init__(self, config: AibaseConfig, http_client: httpx.AsyncClient):
        super().__init__({"aibase": config}, http_client)
        self.ab_config = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.ab_config.enabled:
            return []

        lang = self.ab_config.language if self.ab_config.language in _NEWS_PATH else "en"
        url = _BASE_URL + _NEWS_PATH[lang]

        try:
            response = await self.client.get(url, headers=_HEADERS, follow_redirects=True)
            response.raise_for_status()
        except httpx.HTTPError as exc:
            logger.warning("Error fetching AIbase news: %s", exc)
            return []

        now = datetime.now(timezone.utc)
        soup = BeautifulSoup(response.text, "html.parser")
        items: List[ContentItem] = []

        for anchor in soup.find_all("a", href=re.compile(r"^/(?:zh/)?news/\d+")):
            if len(items) >= self.ab_config.max_items:
                break

            href = anchor.get("href", "")
            article_id = href.rstrip("/").split("/")[-1]
            if not article_id.isdigit():
                continue

            texts = [t.strip() for t in anchor.stripped_strings]
            if len(texts) < 2:
                continue

            # Structure: ['N days ago', '.', 'AIbase', 'Title', 'Description...']
            # or compacted variations; title is the longest short-ish string
            raw_time = texts[0]
            published_at = _parse_relative_time(raw_time, now)
            if published_at is None:
                continue
            if published_at < since:
                continue

            # Title: first text that is not a time/dot/source marker
            title = ""
            description = ""
            for t in texts:
                if _RELATIVE_RE.search(t) or t in (".", "AIbase", "AIbase基地"):
                    continue
                if not title:
                    title = t
                elif not description:
                    description = t
                    break

            if not title:
                continue

            article_url = _BASE_URL + href
            id_hash = hashlib.sha256(article_id.encode()).hexdigest()[:16]

            items.append(
                ContentItem(
                    id=self._generate_id("aibase", "news", id_hash),
                    source_type=SourceType.AIBASE,
                    title=title,
                    url=article_url,
                    content=description or None,
                    author="AIbase",
                    published_at=published_at,
                    metadata={
                        "article_id": article_id,
                        "category": self.ab_config.category,
                        "language": lang,
                    },
                )
            )

        return items
