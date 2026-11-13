# Execution Flow

- Create a pipeline run ID and record start time.
- Run Patient, Encounter, Observation and Condition ingestion sequentially.
- Commit each resource watermark only after raw persistence, Bronze load and batch checks succeed.
- Run Silver, SCD2, Gold and quality notebooks after all resource ingestion activities succeed.
- Record row counts, API request counts, watermarks, exceptions and completion status.
