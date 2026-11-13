"""Ingestion metadata helpers."""
from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def build_ingestion_metadata(resource_type, request_url, batch_id, status_code):
    return {"resource_type": resource_type, "api_url_or_params": request_url,
            "batch_id": batch_id, "http_status": int(status_code),
            "extraction_timestamp": utc_now()}
