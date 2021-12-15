fruits = ["maça", "pera", "laranja", "ovo"]
for fruit in fruits:
    if len(fruit) > 3:
        print(len(fruit))
        print(fruit[3] )
    else:
        print(len(fruit))
        print(fruit[2] )


numero_um = "1"
meu_dic = {numero_um: ["um", "uno", "one"]}
if numero_um in meu_dic:
    print(meu_dic["1"])

meu_dic = {123:"um dois tres", "chave":"valor"}
print(meu_dic[123])
print(meu_dic['chave'])

list_dois = ["dois", "two", "dos", "2"]
print(list_dois)
tupla_dois = tuple(list_dois)
print(tupla_dois)

for item in tupla_dois:
    print(len(item))


list_dois = [ "dois", "two", "dos", "2", "zebu" ]
list_dois.sort()
print(list_dois)
lista_sorted = sorted(list_dois)
print(lista_sorted)

contador = 10
while contador >= 1:
  print(10/contador)
  contador = contador -1
  if contador == 0:
    print("acabou")