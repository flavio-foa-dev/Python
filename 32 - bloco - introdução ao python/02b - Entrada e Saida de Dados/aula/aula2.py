num = 2
print(f"aula: {num} Rodando...")

import json



with open("../data/pokemon.json") as pokemon:
  content = pokemon.read() # leitura do arquivo para jsom
  # print(content)
  pokemon = json.loads(content)["results"] # o conteudo é transformado em estrutura python equivalente, dicionario neste caso
  # acessando a chave result que é onde contem nossa lista de pokemon de
  print("list", pokemon[0]) # imprime a primeira posição da lista

# separamos somente os do type grass
grass_type_poke = [poke for poke in pokemon if "Grass" in poke["type"]]
# print(grass_type_poke)

with open("../data/grass_type_poke.json", mode="w") as file:
  json_to_write = json.dumps(grass_type_poke) # conversao de python para o formato json(str)
  file.write(json_to_write)

with open("../data/grass_type_poke2.json", mode="w") as file:
  # escreve no arquivo ja transfomado em formato jsona estrutura
 json.dump(grass_type_poke, file)

