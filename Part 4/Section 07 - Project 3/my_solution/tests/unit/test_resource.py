# test_resource.py

import pytest

from inventory import Resource

@pytest.fixture
def resource_no_name():
    return Resource('', 'AMD')

@pytest.fixture
def resource_no_mfg():
    return Resource('CPU', '')

@pytest.fixture
def ex_res():
    return Resource('CPU', 'AMD', total=50, allocated=5)

def test_resource_init():
    with pytest.raises(ValueError):
        Resource('', 'AMD')
        Resource('CPU', '')
        

    try:
        resource_no_name
    except ValueError as ex:
        assert str(ex) == 'Name must not be empty.'

    try:
        resource_no_mfg
    except ValueError as ex:
        assert str(ex) == 'Manufacturer must not be empty.'

    try:
        Resource('CPU', 'AMD', 'stuff')
    except TypeError as ex:
        assert str(ex) == 'Value must be an integer.'

    try:
        Resource('CPU', 'AMD', allocated='stuff')
    except TypeError as ex:
        assert str(ex) == 'Value must be an integer.'

def test_resource_purchase(ex_res):
    assert ex_res.total == 50
    assert ex_res.allocated == 5
    assert ex_res.remaining == 45
    ex_res.purchase(30)
    assert ex_res.total == 80

def test_resource_purchase_error(ex_res):
    with pytest.raises(Exception):
        ex_res.purchase(-69)
        ex_res.purchase('many things')

    try:
        ex_res.purchase(0)
    except ValueError as ex:
        assert str(ex) == 'Value must be greater than zero.'
    finally:
        assert ex_res.total == 50
        assert ex_res.allocated == 5
        assert ex_res.remaining == 45

def test_resource_claim(ex_res):
    ex_res.claim(25)
    assert ex_res.total == 50
    assert ex_res.remaining == 20
    assert ex_res.allocated == 30

def test_resource_claim_error(ex_res):
    try:
        ex_res.claim(50)
    except ValueError as ex:
        assert str(ex) == 'Not enough available stock.'
    finally:
        assert ex_res.total == 50
        assert ex_res.allocated == 5
        assert ex_res.remaining == 45

        try:
            ex_res.claim(0)
        except ValueError as ex:
            assert str(ex) == 'Value must be greater than zero.'
        finally:
            assert ex_res.total == 50
            assert ex_res.allocated == 5
            assert ex_res.remaining == 45

def test_resource_freeup(ex_res):
    ex_res.claim(25)
    ex_res.freeup(20)
    assert ex_res.total == 50
    assert ex_res.allocated == 10
    assert ex_res.remaining == 40

def test_resource_died(ex_res):
    ex_res.died(10)
    assert ex_res.total == 40
    assert ex_res.allocated == 5
    assert ex_res.remaining == 35

    ex_res.died(35)
    assert ex_res.total == 5
    assert ex_res.allocated == 5
    assert ex_res.remaining == 0

    ex_res.died(1)
    assert ex_res.total == 4
    assert ex_res.allocated == 4
    assert ex_res.remaining == 0

    with pytest.raises(ValueError):
        ex_res.died(6)
        ex_res.died(0)
        ex_res.died(-1)

def test_resource_str(ex_res):
    assert str(ex_res) == 'CPU'

def test_resource_repr(ex_res):
    assert repr(ex_res) == 'Resource (name=CPU, manufacturer=AMD)'

def test_resource_category(ex_res):
    assert ex_res.category == 'resource'
