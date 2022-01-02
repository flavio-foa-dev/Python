import json
import csv

print("rodando...")



with open("../data/superheroes.json", mode='r') as file:
  hero = json.load(file)
  for h in hero:
    print(h["superhero"])
  # print(json.load(file)[1])
  # print(file.read())


with open("../data/cisade.csv", mode='r') as file:
    local = csv.DictReader(file)
    num = 1
    for l in local:
      print(num, l['ponto_codigo'])
      num =+ 1 # nao consigo fazer ficar dinamico
