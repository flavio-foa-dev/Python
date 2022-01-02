import csv
from analyzer import sales_mivies
from src.importer import importeer_file
print("menu")



def export(data):
  try:
    with open("data/exporte.csv", mode="w") as file:
      report_write = csv.writer(file)
      for key, value in data.items():
        report_write.writerow([key, value])
  except FileNotFoundError:
    print("arquivo nao encontrado")
    return ""

START_MENU = """
1- vendas por Empresa
2- sair
"""


if __name__ == '__main__':
    herois = importeer_file("data/superheroes.json")
    value =  input(f"escola uma opção{START_MENU}")
    if value == "1":
      data = sales_mivies(herois)
      print(data)
      export(data)
    elif value == "2":
      print("saiu")
    else:
      print("opção invalida")