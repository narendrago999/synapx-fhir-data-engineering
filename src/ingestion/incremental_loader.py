"""Incremental FHIR search helpers."""
from datetime import datetime, timezone, timedelta
from .pagination import iter_bundle_pages

def parse_utc(value):
    if isinstance(value, datetime):
        dt = value
    else:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)

def utc_iso(dt):
    return parse_utc(dt).strftime("%Y-%m-%dT%H:%M:%SZ")

def build_search_params(watermark, page_size=100, overlap_minutes=5):
    start = parse_utc(watermark) - timedelta(minutes=overlap_minutes)
    return {"_lastUpdated": f"ge{utc_iso(start)}", "_count": int(page_size)}

def extract_resource(client, resource_type, watermark, page_size=100, overlap_minutes=5):
    if resource_type not in {"Patient", "Encounter", "Observation", "Condition"}:
        raise ValueError(f"Unsupported resource type: {resource_type}")
    url = f"{client.base_url}/{resource_type}"
    params = build_search_params(watermark, page_size, overlap_minutes)
    for page_number, bundle, resolved_url, status in iter_bundle_pages(client, url, params):
        yield {
            "page_number": page_number, "bundle": bundle, "request_url": resolved_url,
            "http_status": status, "extraction_timestamp": utc_iso(datetime.now(timezone.utc)),
            "reported_total": bundle.get("total")
        }
