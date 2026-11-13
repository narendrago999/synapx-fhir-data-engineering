# Data Flow

1. Read the last successful watermark for the resource.
2. Build a FHIR search using _lastUpdated=ge<timestamp>, including a small overlap.
3. Fetch the first Bundle and persist its complete response to Raw.
4. Follow Bundle.link relation=next; validate the host before each request.
5. Record request URL/parameters, extraction timestamp, status, page and batch metadata.
6. Parse Bundle entries into Bronze rows while retaining raw resource JSON.
7. Transform and validate Silver; deduplicate by resource ID and source version.
8. Apply SCD Type 2 to tracked attributes.
9. Build Gold outputs and quality results.
10. Commit the new watermark only after the resource batch succeeds.
