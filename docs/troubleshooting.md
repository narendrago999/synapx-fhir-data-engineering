# Troubleshooting

- HTTP 429/5xx: bounded retry/backoff and retain failed request metadata.
- Pagination loop: track visited next URLs and fail safely.
- Unexpected next host: reject it; never follow cross-host links.
- Empty recent results: report actual source coverage honestly; do not fabricate records.
- Duplicate resources: deduplicate by resource ID and source version while preserving distinct versions.
- Nested fields: retain raw JSON and implement resource-specific parsing.
