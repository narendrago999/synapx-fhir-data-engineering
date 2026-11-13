# Architecture Overview

HAPI FHIR R4 API → immutable Raw JSON page files → Bronze Delta → Silver Delta → Gold analytics outputs → optional Power BI.

| Layer | Responsibility |
|---|---|
| Raw | Original API Bundle payloads partitioned by resource and extraction date |
| Bronze | Resource-level rows retaining raw JSON and source metadata |
| Silver | Typed, standardized, deduplicated resource attributes and references |
| Gold | Analytics-ready entities, measures and reporting views |

Operational tables: metadata_ingestion_log, metadata_watermark, metadata_resource_version, metadata_pipeline_execution.

Use UTC, idempotent batch IDs, overlap windows, bounded retries and update watermarks only after successful validation.
