"""FHIR R4 HTTP client with bounded retries and safe pagination URL validation."""
from __future__ import annotations
from urllib.parse import urlparse
from datetime import datetime, timezone
import time
import requests

class FhirClient:
    def __init__(self, base_url: str, timeout: int = 60, max_retries: int = 3,
                 backoff_seconds=(2, 5, 10), session=None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_seconds = tuple(backoff_seconds)
        self.session = session or requests.Session()
        self.session.headers.update({"Accept": "application/fhir+json"})

    def _validate_url(self, url: str) -> None:
        base, candidate = urlparse(self.base_url), urlparse(url)
        if candidate.scheme != base.scheme or candidate.netloc != base.netloc:
            raise ValueError(f"Refusing URL outside configured FHIR host: {url}")
        if not candidate.path.startswith(base.path):
            raise ValueError(f"Refusing URL outside configured FHIR base path: {url}")

    def get_json(self, url: str, params=None):
        self._validate_url(url)
        last_error = None
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(url, params=params, timeout=self.timeout)
                response.raise_for_status()
                try:
                    payload = response.json()
                except ValueError as exc:
                    raise RuntimeError("FHIR endpoint returned a non-JSON response") from exc
                if not isinstance(payload, dict):
                    raise RuntimeError("FHIR response root must be a JSON object")
                return payload, response.url, response.status_code
            except (requests.RequestException, RuntimeError) as exc:
                last_error = exc
                if attempt + 1 < self.max_retries:
                    delay = self.backoff_seconds[min(attempt, len(self.backoff_seconds)-1)]
                    time.sleep(delay)
        raise RuntimeError(f"FHIR request failed after {self.max_retries} attempts: {last_error}") from last_error

    def server_metadata(self):
        payload, url, status = self.get_json(f"{self.base_url}/metadata")
        return payload, url, status
