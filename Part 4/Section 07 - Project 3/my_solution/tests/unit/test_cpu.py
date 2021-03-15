# test_cpu.py

import pytest

from inventory import Resource, CPU
from copy import deepcopy

@pytest.fixture
def ex_cpu():
    return CPU('Ryzen X900', 'AMD', 8, 'AM4', 130, total=100, allocated=25)

def test_cpu_attributes(ex_cpu):
    assert ex_cpu.cores == 8
    assert ex_cpu.socket == 'AM4'
    assert ex_cpu.power_watts == 130

def test_cpu_str(ex_cpu):
    assert str(ex_cpu) == 'Ryzen X900'

def test_cpu_repr(ex_cpu):
    assert repr(ex_cpu) == 'CPU (name=Ryzen X900, manufacturer=AMD, cores=8, socket=AM4, power=130W)'

def test_cpu_category(ex_cpu):
    assert ex_cpu.category == 'cpu'