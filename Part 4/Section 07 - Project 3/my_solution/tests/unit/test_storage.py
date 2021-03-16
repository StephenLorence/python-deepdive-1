# test_storage.py

import pytest

from inventory import Resource, Storage
from copy import deepcopy

@pytest.fixture
def ex_sto():
    return Storage('12TB Scorpion Black', 'Western Digital', 12_000, 30, 10)

def test_storage_attributes(ex_sto):
    assert ex_sto.capacity_GB == 12_000

def test_storage_str(ex_sto):
    assert str(ex_sto) == '12TB Scorpion Black'

def test_storage_repr(ex_sto):
    assert repr(ex_sto) == 'Storage (name=12TB Scorpion Black, manufacturer=Western Digital, capacity=12000GB)'

def test_storage_category(ex_sto):
    assert ex_sto.category == 'storage'