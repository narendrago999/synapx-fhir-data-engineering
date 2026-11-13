"""FHIR Bundle pagination. Next links are server-provided; page offsets are never inferred."""
from . import __init__  # package marker; no runtime dependency

def next_page_url(bundle):
    for link in bundle.get("link", []) or []:
        if link.get("relation") == "next":
            return link.get("url")
    return None

def iter_bundle_pages(client, first_url, first_params=None, max_pages=10000):
    url, params, visited, page_number = first_url, first_params, set(), 0
    while url:
        if url in visited:
            raise RuntimeError(f"FHIR pagination loop detected: {url}")
        if page_number >= max_pages:
            raise RuntimeError(f"FHIR pagination exceeded max_pages={max_pages}")
        visited.add(url)
        bundle, resolved_url, status = client.get_json(url, params=params)
        if bundle.get("resourceType") != "Bundle":
            raise RuntimeError(f"Expected FHIR Bundle, got {bundle.get('resourceType')}")
        yield page_number, bundle, resolved_url, status
        url = next_page_url(bundle)
        params = None
        page_number += 1
