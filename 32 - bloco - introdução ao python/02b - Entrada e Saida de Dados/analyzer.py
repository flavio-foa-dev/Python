from src.importer import importeer_file

def get_herois(herois):
  pass


if __name__ == '__main__':
  herois = importeer_file("data/superheroes.json")
  print(herois[0])