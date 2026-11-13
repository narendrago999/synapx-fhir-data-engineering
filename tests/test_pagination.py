from src.ingestion.pagination import next_page_url

def test_next_page_url():
    bundle = {"link": [{"relation": "self", "url": "https://example.test/self"},
                       {"relation": "next", "url": "https://example.test/page2"}]}
    assert next_page_url(bundle) == "https://example.test/page2"

def test_no_next_page():
    assert next_page_url({"link": [{"relation": "self", "url": "x"}]}) is None
