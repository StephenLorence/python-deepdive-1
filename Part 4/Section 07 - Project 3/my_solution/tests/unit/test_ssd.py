# test_ssd.py

import pytest

from inventory import Resource, Storage, SSD
from copy import deepcopy

@pytest.fixture
def ex_ssd():
    return SSD('960 Pro', 'Samsung', 500, 'M.2', 100, 35)

def test_ssd_creation_error():
    with pytest.raises(ValueError):
        SSD('960 Pro', 'Samsung', 500, 'm2', 100, 35)
        SSD('960 Pro', 'Samsung', 500, 'test', 100, 35)

def test_ssd_attributes(ex_ssd):
    assert ex_ssd.interface == 'M.2'

def test_ssd_str(ex_ssd):
    assert str(ex_ssd) == '960 Pro'

def test_ssd_repr(ex_ssd):
    assert repr(ex_ssd) == 'SSD (name=960 Pro, manufacturer=Samsung, capacity=500GB, interface=M.2)'

def test_ssd_category(ex_ssd):
    assert ex_ssd.category == 'ssd'