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
    local, * res = csv.DictReader(file)
    print(local)
    # print(res)
    num = 1
    for l in res:
      print(num, l['ponto_codigo'])
      num =+ 1 # nao consigo fazer ficar dinamico
