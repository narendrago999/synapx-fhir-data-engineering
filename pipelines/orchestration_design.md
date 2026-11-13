# Fabric Pipeline Orchestration

Create notebook activities in this strict sequence:
1. Ingest Patient
2. Ingest Encounter
3. Ingest Observation
4. Ingest Condition
5. Bronze processing
6. Silver transformation
7. SCD Type 2 processing
8. Gold transformation
9. Data quality validation

Pass resource_type, watermark and batch/run ID as notebook parameters. Chain activities on success. Stop downstream processing on failure and retain failed-run metadata. Never advance a failed resource watermark.
