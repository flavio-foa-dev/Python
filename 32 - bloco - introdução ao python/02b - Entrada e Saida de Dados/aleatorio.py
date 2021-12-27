print("Maria", "João", "Miguel", "Ana")  # saída: Maria João Miguel Ana
print("Maria", "João", "Miguel", "Ana", sep=",/ ")  # saída: Maria, João, Miguel, Ana



import sys
err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr)

import random

# Já descobri.. Eu não posso ter um arquivo chamado random.py dentro da minha pasta onde está meu código fonte se não ele acha que estou tentando importar um objeto em vez de um módulo... Bom, acho que é isso...

randonm_number = random.randint(1, 15)
print(f"Randonm: {randonm_number}")

menor = int(input("digite manor numero"))
maior = int(input("digite o maior numero"))

print(random.randint(menor, maior))

viloes = ["cuca", "brutos", "esqueleto", "tom"]
person = ["pica-pau", "popay", "hemen", "jerry", "olivia", "shirra"]

v = random.randint(0, 3)
p = random.randint(0, 5)
print(viloes[v], "par com", person[v])