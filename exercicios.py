from random import randint

dice_roll = randint(1, 100)

if dice_roll < 10:
    print("vonte para ono enterios")
elif dice_roll < 20:
    print(f"Sua Nota Foi: {dice_roll} vonte para bimestre anterios ")
elif dice_roll < 30:
    print(f"Sua Nota Foi: {dice_roll} estude para nao repetir voce tera mais uma chance")
elif dice_roll < 50:
    print(f"Sua Nota Foi: {dice_roll} estude para sair da recuperação")
elif dice_roll < 70:
    print(f"Sua Nota Foi: {dice_roll} estude para sair com um sorriso ")
elif dice_roll < 80:
    print(f"Sua Nota Foi: {dice_roll} estudou bem hem ")
elif dice_roll < 95:
    print(f"Sua Nota Foi: {dice_roll} Parabens se estudou bem ")
else:
    print(f"Sua Nota Foi: {dice_roll} Parabens se merece passou direto")
