import json

print("oi")



def importer_pokemon(file_path):
    try:
        with open(file_path) as file_pokemon:
            return json.load(file_pokemon)
    except json.decoder.JSONDecodeError:
      print("Erro no Arquivo")
      return "" # como tera erro no arquivo precisamos retorna algo vazio, para nao quebrar o len

if __name__ == '__main__':
  data = importer_pokemon("./pokemon.json")
  print(len(data))
