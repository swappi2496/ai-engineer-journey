import pytest
from fuel import convert, gauge

def test_convert_basic():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_convert_non_numeric():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("three/four")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_overfull():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("10/3")

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1/-4")

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_normal():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
