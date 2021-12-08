pessoa_trybe = [
  {'nome': 'flavio', 'dominio': 'fullStack', 'idade' :'39'},
  {'nome': 'adao', 'dominio': 'front-end', 'idade' :'35'},
  {'nome': 'antenor', 'dominio': 'bacck-end', 'idade' :'32'},
  ]
print(pessoa_trybe)

dominio = []
for dom in pessoa_trybe:
    dominio.append(dom["nome"])
print(f"esses nome {dominio}")

dominio1 = [dom for dom in pessoa_trybe if dom["nome"] != "antenor"]
print(f"diferente {dominio1}")

dominio2 = [dom["nome"] for dom in pessoa_trybe if dom["nome"] != "antenor"]
print(f"diferente2 {dominio2}")