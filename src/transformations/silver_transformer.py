"""Starter Silver normalization helpers."""
def deduplicate_resource_versions(df):
    return df.dropDuplicates(["resource_type", "resource_id", "source_version_id"])
