import utils

def analize(text):
    report = f"Numero de palavras = {utils.count_words(text)}\n"
    report += f"Numero de letras maisculas = {utils.count_upper_letters(text)}"

    return report

text_to_analize = (
  "Seremos a primeira escolha para quem quer alcançar profissões"
  "digitais na america latina. No Brasil e no mundo milhares de vagas"
  "criadas anualmente no mercado de tecnologias deixam de ser"
  "preenchidas por falta de pessoas qualificadas. Nos trabalhamos duro"
  "todos os dias para que as pessoas tenham a oportunidade de trilhar"
  "esssa carreira eu apoio Att Flavio O, Andrade === Flavio Foa"
)
print(analize(text_to_analize))
