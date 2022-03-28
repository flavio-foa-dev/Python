def analize(text):
    contando_palavras = len(text.split(" "))

    letra_conta = dict()
    for char in text:
        if char in letra_conta:
            letra_conta[char] += 1
        else:
            letra_conta[char] = 1

    return f"numeros de palavras é {letra_conta}"





text = (
    "minha casa de dois dias de sabado "
    "seremos a primeira escola de programação "
    "teremos muitos dinheiro "
    "somo os caras de preto niguem podem "
)
result = len(text)

print((result))

print(analize(text))

