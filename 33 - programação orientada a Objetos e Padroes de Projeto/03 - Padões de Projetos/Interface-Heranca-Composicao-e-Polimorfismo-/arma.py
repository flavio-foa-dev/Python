class Arma:
  def __init__(self, nome, dano):
    self.__nome = nome
    self.__dano = dano

  def get_nome(self):
    return self.__nome

  def get_dano(self):
    return self.__dano
