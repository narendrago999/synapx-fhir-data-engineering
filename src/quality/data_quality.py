"""Reusable data quality checks."""
def assert_required_columns(df, required):
    missing = sorted(set(required) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

def duplicate_count(df, key_columns):
    return df.groupBy(*key_columns).count().filter("count > 1").count()
