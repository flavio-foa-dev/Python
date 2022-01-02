from analyzer import sales_mivies
from src.importer import importeer_file
print("menu")


START_MENU = """
1- vendas por Empresa
2- sair
"""


if __name__ == '__main__':
    herois = importeer_file("data/superheroes.json")
    print(herois)
    value =  input(f"escola uma opção{START_MENU}")
    if value == "1":
      print(sales_mivies(herois))
    elif value == "2":
      print("saiu")
    else:
      print("opção invalida")