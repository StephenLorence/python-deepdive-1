import pytest
from mod import Mod
import os

@pytest.fixture
def create_test_mod():
    return Mod(5, 3)

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

    
def test_mod_creation(create_test_mod):
    assert create_test_mod.value == 2

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

def test_residue_value(create_test_mod):
    assert create_test_mod.value == 2

def test_modulus_value(create_test_mod):
    assert create_test_mod.modulus == 3

def test_read_only_value(create_test_mod):
    with pytest.raises(AttributeError):
        create_test_mod.value = 3

def test_read_only_modulus(create_test_mod):
    with pytest.raises(AttributeError):
        create_test_mod.modulus = 6

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