# Synapx FHIR Data Engineering Assignment

Microsoft Fabric + PySpark implementation of incremental FHIR R4 ingestion from the public HAPI FHIR server.

## Scope
- Resources: Patient, Encounter, Observation, Condition
- Source: https://hapi.fhir.org/baseR4
- Medallion layers: Raw → Bronze → Silver → Gold
- Incremental extraction using `_lastUpdated` and FHIR Bundle pagination
- Original JSON retention, Delta tables, ingestion metadata, SCD Type 2 and data quality
- Required orchestration order: Patient → Encounter → Observation → Condition

> HAPI FHIR is a public test server. Validate actual recent data availability at runtime; do not fabricate source records.

## Repository layout
`architecture/` architecture and data model · `config/` runtime configuration · `notebooks/` Fabric notebooks · `src/` reusable Python modules · `sql/` layer SQL · `pipelines/` orchestration · `tests/` tests · `docs/` operating guides · `screenshots/` execution evidence.

## Reliability rules
1. Follow Bundle links where `relation == "next"`; never assume numeric page offsets.
2. Validate pagination URLs against the configured HAPI host.
3. Persist complete raw API page responses before parsing.
4. Capture extraction/ingestion timestamps, request URL or parameters, batch ID, resource ID, FHIR version ID and source last-updated timestamp.
5. Advance each resource watermark only after its batch succeeds and passes validation.
6. Preserve raw resource JSON; handle nested and polymorphic FHIR fields explicitly.
7. Keep API extraction audit history separate from resource-level SCD Type 2 history.
8. Use PySpark for JSON-to-table conversion; Dataflow Gen2 is not used for that conversion.

## Fabric setup
Create a workspace and Lakehouse named `lh_fhir`, attach it as the default Lakehouse to notebooks, validate API connectivity, then run ingestion in the required order followed by Bronze, Silver, SCD2, Gold and quality checks.

## Status
Initial project scaffold. Complete and execution-test all notebook TODOs and capture Fabric run evidence before submission.
