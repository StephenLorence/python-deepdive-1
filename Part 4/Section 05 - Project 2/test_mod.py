import pytest
from mod import Mod
import os

@pytest.fixture(params=[(5, 3), (7, 2), (16, 5)])
# Apparently when you parametrize a fixture, you need to pass this
# 'request' object in as a parameter to the decorated function, and
# then you can invoke request.param to stand in for each parameter
# in the 'params' list you passed into the decorator.
def create_test_mods(request):
    return Mod(*request.param)

@pytest.fixture
def mod_02():
    return Mod(0, 2)

@pytest.fixture
def mod_22():
    return Mod(2, 2)

@pytest.fixture
def mod_53():
    return Mod(5, 3)

@pytest.fixture
def mod_127():
    return Mod(12, 7)

    
def test_mod_creation(mod_53):
    assert mod_53.value == 2

def test_negative_modulus():
    with pytest.raises(ValueError):
        m = Mod(5, -3)

def test_non_int_value():
    with pytest.raises(TypeError):
        m = Mod('test', 3)

def test_non_int_modulus():
    with pytest.raises(TypeError):
        m = Mod(5, 'test')

def test_multiple_mods(create_test_mods):
    assert create_test_mods.value % create_test_mods.modulus == create_test_mods.value

def test_residue_value(mod_53):
    assert mod_53.value == 2

def test_modulus_value(mod_53):
    assert mod_53.modulus == 3

def test_read_only_value(mod_53):
    with pytest.raises(AttributeError):
        mod_53.value = 3

def test_read_only_modulus(mod_53):
    with pytest.raises(AttributeError):
        mod_53.modulus = 6

def test_equal_2_mods(mod_02, mod_22):
    assert mod_02 == mod_22

def test_equal_mod_int(mod_02):
    assert mod_02 == 2

def test_equal_int_mod(mod_22):
    assert 6 == mod_22

def test_not_equal_mod_str(mod_02):
    assert mod_02 != 'test string'

def test_not_equal_mod_int(mod_22):
    assert mod_22 != 3

def test_not_equal_2_mods(mod_22, mod_53):
    assert mod_22 != mod_53

def test_equal_mod_equal_hash(mod_02, mod_22):
    assert hash(mod_02) == hash(mod_22)

def test_unequal_mod_unequal_hash(mod_22, mod_53):
    assert hash(mod_22) != hash(mod_53)

def test_int_from_mod(mod_22, mod_53):
    assert (int(mod_22), int(mod_53)) == (0, 2)

def test_mod_str(mod_53):
    assert str(mod_53) == 'Mod(value=2, modulus=3)'

def test_mod_repr(mod_22):
    assert repr(mod_22) == 'Mod(value=0, modulus=2)'

@pytest.mark.parametrize('test_value, expected', [
                                                  (Mod(5, 3), ValueError),
                                                  (Mod(7, 2), 1),
                                                  (Mod(16, 5), ValueError),
                                                  (5, 1),
                                                  (2, 0)
                                                  ])
def test_mod_add(mod_02, test_value, expected):
    if type(expected) == type and issubclass(expected, Exception):
        with pytest.raises(ValueError):
            mod_02 + test_value
    else:
        assert mod_02 + test_value == expected

@pytest.mark.parametrize('test_value, expected', [
                                                  (Mod(5, 3), ValueError),
                                                  (Mod(7, 2), 1),
                                                  (Mod(16, 5), ValueError),
                                                  (5, 1),
                                                  (2, 0)
                                                  ])
def test_mod_sub(mod_02, test_value, expected):
    if type(expected) == type and issubclass(expected, Exception):
        with pytest.raises(ValueError):
            mod_02 - test_value
    else:
        assert mod_02 - test_value == expected

@pytest.mark.parametrize('test_value, mod_22_result, mod_127_result', [
                                                  (Mod(5, 3), ValueError, ValueError),
                                                  (Mod(7, 2), 0, ValueError),
                                                  (Mod(16, 5), ValueError, ValueError),
                                                  (5, 0, 4),
                                                  (2, 0, 3),
                                                  (Mod(3, 7), ValueError, 1)
                                                  ])
def test_mod_mul(mod_22, mod_127, test_value, mod_22_result, mod_127_result):
    if type(mod_22_result) == type and issubclass(mod_22_result, Exception):
        with pytest.raises(ValueError):
            mod_22 * test_value
    else:
        assert mod_22 * test_value == mod_22_result
    if type(mod_127_result) == type and issubclass(mod_127_result, Exception):
        with pytest.raises(ValueError):
            mod_127 * test_value
    else:
        assert mod_127 * test_value == mod_127_result

@pytest.mark.parametrize('test_value, mod_22_result, mod_127_result', [
                                                  (Mod(5, 3), ValueError, ValueError),
                                                  (Mod(7, 2), 0, ValueError),
                                                  (Mod(16, 5), ValueError, ValueError),
                                                  (5, 0, 3),
                                                  (2, 1, 4),
                                                  (0, 1, 1),
                                                  (Mod(3, 7), ValueError, 6)
                                                  ])
def test_mod_pow(mod_22, mod_127, test_value, mod_22_result, mod_127_result):
    if type(mod_22_result) == type and issubclass(mod_22_result, Exception):
        with pytest.raises(ValueError):
            mod_22 ** test_value
    else:
        assert mod_22 ** test_value == mod_22_result
    if type(mod_127_result) == type and issubclass(mod_127_result, Exception):
        with pytest.raises(ValueError):
            mod_127 ** test_value
    else:
        assert mod_127 ** test_value == mod_127_result