import json

print("rodando")




def importeer_file(file_path):
    try:
        with open(file_path) as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        print("Erro no Arquivo")
        return "" # como tera erro no arquivo precisamos retorna algo vazio, para nao quebrar o len
    except FileNotFoundError:
        print("Erro no caminho do Arquivo")
        return ""

if __name__ == '__main__':
  data = importeer_file("data/superheroes.json")
  print(f"o tamanho é: {len(data)}")
