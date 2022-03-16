from personagem_ofensivo import PersonagemOfensivo
from personagem_defensivo import PersonagemDefensivo
from arma import Arma


daniel = PersonagemDefensivo('Daniel', 100)
espada = Arma('espada', 75)
lawrence = PersonagemOfensivo('Lawrence', 100, 50)

lawrence.set_arma(espada)

print(daniel.falar())
print(lawrence.falar())
print(daniel.defender(lawrence.atacar()))
print(daniel.falar())





