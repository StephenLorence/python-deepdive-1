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
    with pytest.raises(ValueError):
        validate_hdd_form_factor('test')
        validate_hdd_form_factor(2.3)

    assert validate_hdd_form_factor(2.5) == '2.5"'
    assert validate_hdd_form_factor('"2.5"') == '2.5"'
    assert validate_hdd_form_factor(3.5) == '3.5"'
    assert validate_hdd_form_factor('""3.5""') == '3.5"'

def test_validate_hdd_rpm():
    for num in [1234, 999999999]:
        try:
            validate_hdd_rpm(1234)
            assert False
        except ValueError as ex:
            assert str(ex) == 'RPM must be between 5,000 and 15,000 RPM.'

    for num in [12345, 11111, 6969]:
        try:
            validate_hdd_rpm(12345)
            assert False
        except ValueError as ex:
            assert str(ex) == 'RPM must be a multiple of 100.'

    assert validate_hdd_rpm(12000) == 12000


    # if not (5_000 <= value <= 15_000):
    #     raise ValueError('RPM must be between 5,000 and 15,000 RPM.')
    # if value % 100:
    #     raise ValueError('RPM must be a multiple of 100.')

def test_validate_ssd_interface():
    with pytest.raises(ValueError):
        for item in ['pci', 'pcix', 'pciea',
                     1, 0, '', '_', 'm2']:
            validate_ssd_interface('pci')
    assert validate_ssd_interface('pcie') == 'PCIe'
    assert validate_ssd_interface('msaTA') == 'mSATA'
    assert validate_ssd_interface('m.2') == 'M.2'

    