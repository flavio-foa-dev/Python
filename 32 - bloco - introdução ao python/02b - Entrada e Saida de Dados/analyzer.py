from src.importer import importeer_file

def get_herois(herois):
  #print(herois)

  hero = set()
  for h in herois:
    hero.add(h["publisher"])
  return hero

if __name__ == '__main__':
  herois = importeer_file("data/superheroes.json")
  print(get_herois(herois))