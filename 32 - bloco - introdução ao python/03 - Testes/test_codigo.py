from codigo import is_odd

def test_is_odd_when_number_is_odd_returns_true():
  'Para umnumero ímpar a função deve retornar o valor True'
  assert is_odd(3) is True #true tem ser letra maiscula

def test_is_odd_when_number_is_evem_returns_false():
  'Para um numero par a função deve retornar o valor false'
  assert is_odd(2) is False # False tem que ser letra maiscula