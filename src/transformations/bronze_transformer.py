"""Convert FHIR Bundle entries to Bronze rows while retaining full resource JSON."""
import json

def bundle_to_bronze_rows(bundle, resource_type, extraction_timestamp, api_url_or_params, batch_id):
    rows = []
    for entry in bundle.get("entry", []) or []:
        resource = entry.get("resource")
        if not isinstance(resource, dict):
            continue
        if resource.get("resourceType") != resource_type:
            raise ValueError(f"Bundle entry resourceType mismatch: expected {resource_type}, got {resource.get('resourceType')}")
        meta = resource.get("meta") or {}
        rows.append({
            "resource_type": resource_type,
            "resource_id": resource.get("id"),
            "source_version_id": meta.get("versionId"),
            "source_last_updated": meta.get("lastUpdated"),
            "extraction_timestamp": extraction_timestamp,
            "ingestion_timestamp": extraction_timestamp,
            "api_url_or_params": api_url_or_params,
            "batch_id": batch_id,
            "raw_resource_json": json.dumps(resource, separators=(",", ":"), ensure_ascii=False)
        })
    return rows
