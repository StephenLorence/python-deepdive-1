# test_validator.py

import pytest

from validators import validate_string, validate_integer

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