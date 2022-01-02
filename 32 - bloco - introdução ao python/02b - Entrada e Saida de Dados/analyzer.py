from src.importer import importeer_file

def get_herois(herois):
  #print(herois)

  hero = set()
  for h in herois:
    hero.add(h["publisher"])
  return hero

def sales_mivies(herois):
  result_sale = { price:0 for price in get_herois(herois) }

  for h in herois:
      hero = h["publisher"]
      result_sale[hero]+=int(h["price"]["valor"])

  return result_sale

if __name__ == '__main__':
  herois = importeer_file("data/superheroes.json")
  print(get_herois(herois))
  print(sales_mivies(herois))