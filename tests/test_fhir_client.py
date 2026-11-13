import pytest
from src.ingestion.fhir_client import FhirClient

def test_rejects_external_pagination_url():
    client = FhirClient("https://hapi.fhir.org/baseR4")
    with pytest.raises(ValueError):
        client._validate_url("https://example.org/baseR4/Patient")
