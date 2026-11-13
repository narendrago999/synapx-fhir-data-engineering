# Common Lineage Data Dictionary

| Column | Meaning |
|---|---|
| resource_type | FHIR resource type |
| resource_id | FHIR logical ID |
| source_version_id | FHIR meta.versionId, when present |
| source_last_updated | FHIR meta.lastUpdated, when present |
| extraction_timestamp | UTC API retrieval timestamp |
| ingestion_timestamp | UTC persistence timestamp |
| api_url_or_params | Request URL or serialized search parameters |
| batch_id | Unique ingestion batch/run identifier |
| raw_resource_json | Original resource JSON |
| valid_from / valid_to | SCD2 validity interval |
| is_active | Current SCD2 version indicator |
