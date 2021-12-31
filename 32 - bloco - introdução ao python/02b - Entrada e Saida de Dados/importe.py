import json

print("oi")



def importer_pokemon(file_path):
    try:
        with open(file_path) as file_pokemon:
            return json.load(file_pokemon)
    except json.decoder.JSONDecodeError:
      print("Erro no Arquivo")
      return "" # como tera erro no arquivo precisamos retorna algo vazio, para nao quebrar o len
    except FileNotFoundError:
      print("Erro no caminho do Arquivo")
      return ""

def get_pokemons(pokemon):
  pokemons = set()
  for p in pokemon:
    pokemons.add(p["name"])
  return pokemons


if __name__ == '__main__':
  data = importer_pokemon("./pokemon.json")
  print(len(data))
  print(data[0]["name"])

  pokemons = get_pokemons(data)
  print(pokemons)
