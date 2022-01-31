import py
import pytest

def test_m4():
    assert False
#test with markers
@pytest.mark.home
def test_m5():
    assert 100 == 100

def test_m6():
    assert "Mukund" == "MUKUND"
#test cases with markers
@pytest.mark.home
def test_login():
    assert "admin" == "admin"

