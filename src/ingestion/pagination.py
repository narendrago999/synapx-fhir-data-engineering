"""FHIR Bundle pagination helpers."""
def next_page_url(bundle):
    for link in bundle.get("link", []):
        if link.get("relation") == "next":
            return link.get("url")
    return None

def iter_bundle_pages(client, first_url, first_params=None):
    url, params, visited = first_url, first_params, set()
    while url:
        if url in visited:
            raise RuntimeError(f"Pagination loop detected at {url}")
        visited.add(url)
        bundle, resolved_url, status = client.get_json(url, params=params)
        yield bundle, resolved_url, status
        url = next_page_url(bundle)
        params = None
