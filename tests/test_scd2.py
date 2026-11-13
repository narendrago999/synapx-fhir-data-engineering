def test_scd2_contract_is_documented():
    from pathlib import Path
    text = Path("src/history/scd_type2.py").read_text(encoding="utf-8")
    assert "SCD Type 2" in text
