from abc import ABC, abstractmethod

class PersonagemInterface(ABC):
  @abstractmethod
  def reduzir_hp(self, dano):
    raise NotImplementedError

  @abstractmethod
  def falar(self):
    raise NotImplementedError
