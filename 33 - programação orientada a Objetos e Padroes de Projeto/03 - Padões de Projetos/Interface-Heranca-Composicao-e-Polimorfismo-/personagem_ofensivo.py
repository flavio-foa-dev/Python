from personagem import Personagem 

class PersonagemOfensivo(Personagem):
  def __init__(self, nome, hp, dano, arma = None):
    super().__init__(nome, hp)
    self.__dano = dano
    self.__arma = arma

  def set_arma(self, arma):
    self.__arma = arma
  
  def atacar(self):
    if self.__arma:
      print(f"{self.get_nome()} atacou com {self.__arma.get_nome()}.")
      return self.__arma.get_dano()
    print(f"{self.get_nome()} atacou sem arma.")
    return self.__dano

  def falar(self):
    fala = f'Eu sou o poderoso {self.get_nome()}'
    if self.get_hp() > 0:
      return f'{fala}, ainda estou vivinho, com {self.get_hp()} de vida ainda, seu inseto'
    return fala + ' e morri. Nãããoooo =('
