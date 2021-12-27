email_file = open("email-clientes.txt", mode="w") # abrimos o arquivo, se nao existir criamos

email_file.write("foa12381@gmail.com\n")
email_file.write("foa12380@gmail.com\n")



more_email = [
  "foa12381@gmail.com\n",
   "foa12381@gmail.com\n",
    "foa12381@gmail.com\n",
     "foa12381@gmail.com\n" # aqui temos que colocar \n para pulkar linhas
]
email_file.writelines(more_email)

print("foa221@hotmail", file=email_file) #print ja escreve e pula linha
print("foa221@hotmail", file=email_file)
print("foa221@hotmail", file=email_file)

email_file.writelines(["um\n", "dois\n", "tres\n", "quatro\n"]) # podemos escrever multiplos arquivos e pular linhas com \n em cada escrita


email_file.close()

file_email = open("email-clientes.txt", mode="r")

content = file_email.read()

print("este", content)

for line in file_email:
  print(f"o email è {line}")

file_email.close() # fechamos o arquivo

