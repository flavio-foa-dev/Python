def analize(text):
    text = text.split(' ')
    print(text)
    print(len(text))

    cout_upper_letters = 0
    for char in text:
        if char[0].isupper():
            cout_upper_letters += 1
    print(cout_upper_letters)

text_to_analize = (
  "Seremos a primeira escolha para quem quer alcançar profissões"
  "digitais na america latina. No Brasil e no mundo milhares de vagas"
  "criadas anualmente no mercado de tecnologias deixam de ser"
  "preenchidas por falta de pessoas qualificadas. Nos trabalhamos duro"
  "todos os dias para que as pessoas tenham a oportunidade de trilhar"
  "esssa carreira eu apoio Att Flavio O, Andrade === Flavio Foa"
)
analize(text_to_analize)
