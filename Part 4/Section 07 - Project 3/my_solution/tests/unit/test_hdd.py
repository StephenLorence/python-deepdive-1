# test_hdd.py

import pytest

from inventory import Resource, Storage, HDD
from copy import deepcopy

@pytest.fixture
def ex_hdd():
    return HDD('12TB Scorpion Black', 'Western Digital', 12_000, 3.5, 7200, 30, 10)

def test_hdd_creation_error():
    with pytest.raises(ValueError):
        HDD('12TB Scorpion Black', 'Western Digital', 12_000, 2.5, 1234)
        HDD('12TB Scorpion Black', 'Western Digital', 12_000, 2.1, 7200)

def test_hdd_attributes(ex_hdd):
    assert ex_hdd.capacity_GB == 12_000

def test_hdd_str(ex_hdd):
    assert str(ex_hdd) == '12TB Scorpion Black'

def test_hdd_repr(ex_hdd):
    assert repr(ex_hdd) == 'HDD (name=12TB Scorpion Black, manufacturer=Western Digital, capacity=12000GB, size=3.5", rpm=7200)'

def test_hdd_category(ex_hdd):
    assert ex_hdd.category == 'hdd'