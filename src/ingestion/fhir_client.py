"""FHIR HTTP client with bounded retries and pagination URL validation."""
from urllib.parse import urlparse
import time
import requests

class FhirClient:
    def __init__(self, base_url, timeout=60, max_retries=3):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/fhir+json"})

    def get_json(self, url, params=None):
        self._validate_url(url)
        last_error = None
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(url, params=params, timeout=self.timeout)
                response.raise_for_status()
                return response.json(), response.url, response.status_code
            except Exception as exc:
                last_error = exc
                if attempt + 1 < self.max_retries:
                    time.sleep([2, 5, 10][min(attempt, 2)])
        raise RuntimeError(f"FHIR request failed after retries: {last_error}") from last_error

    def _validate_url(self, url):
        base, candidate = urlparse(self.base_url), urlparse(url)
        if candidate.scheme != base.scheme or candidate.netloc != base.netloc:
            raise ValueError(f"Refusing pagination URL outside configured host: {url}")
