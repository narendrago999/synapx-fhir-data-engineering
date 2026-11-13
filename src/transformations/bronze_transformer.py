"""Convert FHIR Bundle entries to resource-level Bronze records."""
import json

def bundle_to_bronze_rows(bundle, resource_type, extraction_timestamp, api_url_or_params, batch_id):
    rows = []
    for entry in bundle.get("entry", []):
        resource = entry.get("resource")
        if not resource:
            continue
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
