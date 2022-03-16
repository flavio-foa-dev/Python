from personagem_interface import PersonagemInterface


class Personagem(PersonagemInterface):
  def __init__(self, nome, hp):
    self.__nome = nome
    self.__hp = hp

  def reduzir_hp(self, dano):
    self.__hp -= dano
  
  def falar(self):  
    fala = f'Eu sou o {self.__nome}'
    if self.__hp > 0:
      return f'{fala}, ainda estou vivo, com {self.__hp} de vida'
    return fala + ' e morri =('

  def get_hp(self):
    return self.__hp

  def get_nome(self):
    return self.__nome
