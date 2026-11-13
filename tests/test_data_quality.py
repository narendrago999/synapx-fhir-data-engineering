import pytest
from src.quality.data_quality import assert_required_columns

class FakeDF:
    columns = ["resource_id", "resource_type"]

def test_required_columns_pass():
    assert_required_columns(FakeDF(), ["resource_id"])

def test_required_columns_fail():
    with pytest.raises(ValueError):
        assert_required_columns(FakeDF(), ["missing"])
