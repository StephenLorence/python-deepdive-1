# test_resource.py

import pytest

from inventory import Resource, CPU, Storage, HDD, SSD
from copy import deepcopy

res_list = [Resource('CPU', 'AMD', total=50, allocated=5),
            CPU('Ryzen X900', 'AMD', 8, 'AM4', 130, total=50, allocated=5),
            Storage('12TB Scorpion Black', 'Western Digital', 12_000, 50, 5),
            HDD('12TB Scorpion Black', 'Western Digital', 12_000, 3.5, 7200, 50, 5),
            SSD('960 Pro', 'Samsung', 500, 'M.2', 50, 5)]

@pytest.fixture
def resource_no_name():
    return Resource('', 'AMD')

@pytest.fixture
def resource_no_mfg():
    return Resource('CPU', '')

@pytest.fixture
def ex_resource():
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

@pytest.mark.parametrize('ex_res', deepcopy(res_list))
def test_resource_purchase(ex_res):
    assert ex_res.total == 50
    assert ex_res.allocated == 5
    assert ex_res.remaining == 45
    ex_res.purchase(30)
    assert ex_res.total == 80

@pytest.mark.parametrize('ex_res', deepcopy(res_list))
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

@pytest.mark.parametrize('ex_res', deepcopy(res_list))
def test_resource_claim(ex_res):
    ex_res.claim(25)
    assert ex_res.total == 50
    assert ex_res.remaining == 20
    assert ex_res.allocated == 30

@pytest.mark.parametrize('ex_res', deepcopy(res_list))
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

@pytest.mark.parametrize('ex_res', deepcopy(res_list))
def test_resource_freeup(ex_res):
    ex_res.claim(25)
    ex_res.freeup(20)
    assert ex_res.total == 50
    assert ex_res.allocated == 10
    assert ex_res.remaining == 40

@pytest.mark.parametrize('ex_res', deepcopy(res_list))
def test_resource_died(ex_res):
    ex_res.died(3)
    assert ex_res.total == 47
    assert ex_res.allocated == 2
    assert ex_res.remaining == 45

    ex_res.died(2)
    assert ex_res.total == 45
    assert ex_res.allocated == 0
    assert ex_res.remaining == 45

    with pytest.raises(ValueError):
        ex_res.died(6)
        ex_res.died(0)
        ex_res.died(-1)

def test_resource_str(ex_resource):
    assert str(ex_resource) == 'CPU'

def test_resource_repr(ex_resource):
    assert repr(ex_resource) == 'Resource (name=CPU, manufacturer=AMD)'

def test_resource_category(ex_resource):
    assert ex_resource.category == 'resource'
