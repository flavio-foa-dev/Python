meu_dict = 123
print(meu_dict)

lista_frutas = ['banana', 'uvaa', 'maça', 'pera']

for fruta in lista_frutas:
  print(fruta[3])

numero_um = "1"
meu_dict ={numero_um:["um", "one", "uno"]}

if numero_um in meu_dict:
  print(meu_dict['1'])

meu_dict = {123: "um dois tres", "chave": "valor"}
print(meu_dict[123])
print(meu_dict["chave"])

for index in range(5):
    print(f"index {index + 1}")

n = 10
last, next = 0, 1
while last < n:
    print(f"Fibonacci {last}")
    last, next = next, last + next

def imc (peso, altura ):
    result = peso/(altura /100)**2
    print(f"seu imc e {result}")

imc(100, 187)
imc(peso=90, altura=187)

# contador = 10
# while catador > 0:
#   print(10/contador)
#   contador -= 1