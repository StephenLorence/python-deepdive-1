# test_validator.py

import pytest

from validators import (validate_string, validate_integer,
                       validate_hdd_form_factor, validate_hdd_rpm,
                       validate_ssd_interface)

def test_validate_string():
    with pytest.raises(ValueError):
        validate_string('', 'Name')

    assert validate_string('test', 'Name') == 'test'

def test_validate_integer():
    with pytest.raises(TypeError):
        validate_integer('hello')
    with pytest.raises(ValueError):
        validate_integer(-1)

    assert validate_integer(15) == 15
    assert validate_integer('200') == 200
    assert validate_integer(12.0) == 12

def test_validate_hdd_form_factor():

def test_validate_hdd_rpm():

def test_validate_ssd_interface():
    