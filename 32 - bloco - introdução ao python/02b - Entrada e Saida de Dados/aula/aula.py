import json
import csv

print("rodando...")



with open("../data/superheroes.json", mode='r') as file:
  print(json.load(file)[1])
  print(file.read())


# with open("../data/cisade.csv", mode='r') as file:
#   print(file.read())