# Logical Data Model

- Patient: identity and demographic attributes.
- Encounter: visit context; may reference Patient.
- Observation: measurement/result; may reference Patient and Encounter.
- Condition: diagnosis/problem; may reference Patient and Encounter.

Common lineage: resource_type, resource_id, source_version_id, source_last_updated, extraction_timestamp, ingestion_timestamp, batch_id, api_url_or_params, raw_resource_json.

Retain FHIR references as supplied (for example Patient/123). Resolve them to model keys in Silver/Gold only when the referenced resource is available. Do not assume related resources arrive in the same incremental batch.
