arquivos = []
for i in range(10): # colocando mais de 8167 quebra o sistema teste
  arquivos.append(open(f"arquivo{i}.txt", mode="w"))

arquivos.close()