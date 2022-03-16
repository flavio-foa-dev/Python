from personagem import Personagem
from random import choice

class PersonagemDefensivo(Personagem):
  def __init__(self, nome, hp):
    super().__init__(nome, hp)

  def defender(self, dano):
    defesa = choice([True, False])
    if defesa:
      return f'{self.get_nome()} defendeu'

    self.reduzir_hp(dano)
    return f'{self.get_nome()} apanhou, hp: {self.get_hp()}'
