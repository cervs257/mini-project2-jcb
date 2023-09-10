from main import create_ticker


def test_create_ticker():
    assert create_ticker("usdmxn") == "USDMXN=X"
