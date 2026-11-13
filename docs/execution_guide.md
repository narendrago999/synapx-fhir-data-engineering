# Execution Guide

Run API validation first. Ingest Patient, Encounter, Observation and Condition in that exact order. Confirm Raw files and Bronze Delta rows after each resource. Then execute Silver, SCD2, Gold and quality processing. Capture run IDs, row counts, watermarks, request counts and exceptions as submission evidence.
