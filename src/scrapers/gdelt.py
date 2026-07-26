"""GDELT 2.0 DOC API scraper.

Pulls recent global news articles from the key-less GDELT 2.0 DOC API
(https://api.gdeltproject.org/api/v2/doc/doc) and maps them into
ContentItem instances so the rest of the Horizon pipeline (deduplication,
AI scoring, enrichment, summarization) treats them the same way as RSS or
Hacker News items.

Design notes:

* No API key is required; GDELT is fully open. The DOC API caps results at
  250 records per request, so `max_records` is kept modest by default.
* GDELT expresses source-language and source-country filters as query
  operators (``sourcelang:`` / ``sourcecountry:``) rather than separate
  parameters, so they are appended to the query string.
* GDELT can return non-JSON or empty bodies on transient errors, so the
  ``.json()`` call is guarded and an empty/missing ``articles`` key yields
  an empty list rather than raising.
* A single malformed article is skipped, not allowed to abort the batch.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any, List, Optional

import httpx

from .base import BaseScraper
from ..models import ContentItem, GDELTConfig, SourceType

logger = logging.getLogger(__name__)


class GDELTScraper(BaseScraper):
    """Scraper backed by the GDELT 2.0 DOC API."""

    SOURCE_TYPE = SourceType.GDELT
    BASE_URL = "https://api.gdeltproject.org/api/v2/doc/doc"

    def __init__(self, configs: List[GDELTConfig], http_client: httpx.AsyncClient):
        super().__init__({"gdelt": configs}, http_client)
        self.configs = configs

    async def fetch(self, since: datetime) -> List[ContentItem]:
        items: List[ContentItem] = []
        for cfg in self.configs:
            items.extend(await self._fetch_one(cfg, since))
        return items

    async def _fetch_one(self, cfg: GDELTConfig, since: datetime) -> List[ContentItem]:
        """Fetch articles for a single GDELTConfig entry."""
        if not cfg.enabled:
            return []

        if cfg.stocks:
            query = " OR ".join(f'"{s}"' for s in cfg.stocks)
        else:
            query = (cfg.query or "").strip()
        if not query:
            return []

        if cfg.language:
            query = f"{query} sourcelang:{cfg.language}"
        if cfg.country:
            query = f"{query} sourcecountry:{cfg.country}"

        params: dict[str, Any] = {
            "query": query,
            "mode": cfg.mode,
            "format": "json",
            "maxrecords": cfg.max_records,
            "sort": "datedesc",
        }

        if cfg.timespan:
            params["timespan"] = cfg.timespan
        else:
            since_utc = self._ensure_utc(since)
            now_utc = datetime.now(timezone.utc)
            params["startdatetime"] = since_utc.strftime("%Y%m%d%H%M%S")
            params["enddatetime"] = now_utc.strftime("%Y%m%d%H%M%S")

        try:
            response = await self.client.get(
                self.BASE_URL, params=params, follow_redirects=True
            )
            response.raise_for_status()
            try:
                payload = response.json()
            except Exception as exc:
                logger.warning("GDELT returned a non-JSON body: %s", exc)
                return []
            if not isinstance(payload, dict):
                return []
            articles = payload.get("articles")
            if not articles:
                return []
            items: List[ContentItem] = []
            for raw in articles:
                item = self._raw_to_item(raw, cfg)
                if item is not None:
                    items.append(item)
            return items
        except httpx.HTTPError as exc:
            logger.warning("Error fetching GDELT articles: %s", exc)
            return []
        except Exception as exc:
            logger.warning("Error parsing GDELT response: %s", exc)
            return []

    def _raw_to_item(self, raw: Any, cfg: GDELTConfig) -> Optional[ContentItem]:
        """Map one GDELT article record into a ContentItem.

        Returns None when the record has no URL/title or an unparseable
        ``seendate`` (published_at is required), so a single bad article is
        skipped rather than aborting the batch.
        """
        if not isinstance(raw, dict):
            return None

        url = (raw.get("url") or "").strip()
        title = (raw.get("title") or "").strip()
        if not url or not title:
            return None

        seendate = (raw.get("seendate") or "").strip()
        published = self._parse_seendate(seendate)
        if published is None:
            return None

        native_id = f"{seendate}::{url}"
        meta = {
            "domain": raw.get("domain"),
            "sourcecountry": raw.get("sourcecountry"),
            "language": raw.get("language"),
            "query": cfg.query,
            "category": cfg.category,
        }

        try:
            return ContentItem(
                id=self._generate_id("gdelt", "article", native_id),
                source_type=self.SOURCE_TYPE,
                title=title,
                url=url,
                content=None,
                author=raw.get("domain"),
                published_at=published,
                metadata={k: v for k, v in meta.items() if v is not None},
            )
        except Exception as exc:
            logger.warning("Skipping invalid GDELT article %s: %s", url, exc)
            return None

    @staticmethod
    def _parse_seendate(value: str) -> Optional[datetime]:
        """Parse a GDELT ``seendate`` ("YYYYMMDDTHHMMSSZ") into aware UTC."""
        if not value:
            return None
        try:
            dt = datetime.strptime(value, "%Y%m%dT%H%M%SZ")
        except (ValueError, TypeError):
            return None
        return dt.replace(tzinfo=timezone.utc)

    @staticmethod
    def _ensure_utc(moment: datetime) -> datetime:
        if moment.tzinfo is None:
            return moment.replace(tzinfo=timezone.utc)
        return moment.astimezone(timezone.utc)
