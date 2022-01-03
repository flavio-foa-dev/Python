num = 3
print(f"aula: {num} Rodando...")

import csv


a, b = "cd"
print(a)  # saída: c
print(b)  # saída: d

head, *tail = [1,2,3] # Quando um * está presente no desempacotamento, os valores são desempacotados em formato de lista.
print(head)  # saída: 1
print(tail)  # saída: [2, 3]


with open("../data/vide_game.csv",mode="r", encoding="utf8") as file:
  # print(file.read())
  game = csv.reader(file, delimiter=",", quotechar='"')
  header, *data = game
  print(header)
  print(data[0])

for i in data:
    game = i[1]
    console = i[2]
    print(game,console )


with open("../data/vide_game.csv") as file:
  game = csv.DictReader(file, delimiter=",", quotechar='"')
# a linha  de cabeçalho é utilizada  como chave do dicionario, agrupa campanhas e suas respectivas balneabilidades
  consoles = {}