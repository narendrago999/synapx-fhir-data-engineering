"""SCD Type 2 implementation contract.

Implement with Spark and Delta MERGE:
1. Hash tracked business attributes for each resource ID.
2. Compare incoming hashes with the active version.
3. Expire changed active rows (valid_to, is_active=false).
4. Insert new/changed versions (valid_from, valid_to=null, is_active=true).
5. Do not create a version when tracked attributes are unchanged.
6. Preserve FHIR meta.versionId/meta.lastUpdated separately from SCD validity.

Keep API extraction audit events separate from resource business history.
"""
