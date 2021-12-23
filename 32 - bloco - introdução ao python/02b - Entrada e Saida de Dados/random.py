print("Maria", "João", "Miguel", "Ana")  # saída: Maria João Miguel Ana
print("Maria", "João", "Miguel", "Ana", sep=", ")  # saída: Maria, João, Miguel, Ana





import sys
err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr)