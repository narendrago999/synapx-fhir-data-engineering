"""Incremental FHIR extraction primitives."""
from datetime import datetime, timezone, timedelta
from .pagination import iter_bundle_pages

def utc_iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def build_search_params(watermark, page_size=100, overlap_minutes=5):
    start = watermark - timedelta(minutes=overlap_minutes)
    return {"_lastUpdated": f"ge{utc_iso(start)}", "_count": page_size}

def extract_resource(client, resource_type, watermark, page_size=100):
    url = f"{client.base_url}/{resource_type}"
    params = build_search_params(watermark, page_size)
    for bundle, resolved_url, status in iter_bundle_pages(client, url, params):
        yield {"bundle": bundle, "request_url": resolved_url, "http_status": status,
               "extraction_timestamp": utc_iso(datetime.now(timezone.utc))}
