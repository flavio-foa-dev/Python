numero = input("Digite seu Nome: ")
print(f"Seja bem vindo {numero} !")
for i in numero:
  print(i)

meu_numero1 = 0
while meu_numero1 < 50:
    try:
        meu_numero = int(input("Digite um numero: "))
    except ValueError:
        print("Não é número")
        break
    meu_numero1 += meu_numero

if meu_numero1< 50:
  print("tente novamente")
if meu_numero >= 50:
  print(f"seu nomero é maior que 50 valor final {meu_numero1}")

