import pytest
from codigo import is_odd, is_divide


def test_is_odd_when_number_is_odd_returns_true():
  'Para umnumero ímpar a função deve retornar o valor True'
  assert is_odd(3) is True #true tem ser letra maiscula

def test_is_odd_when_number_is_evem_returns_false():
  'Para um numero par a função deve retornar o valor false'
  assert is_odd(2) is False # False tem que ser letra maiscula

def test_is_divide_trows_exception_when_dividing_by_zero():
  with pytest.raises( ZeroDivisionError,match='division by zero'):
    is_divide(2,0)