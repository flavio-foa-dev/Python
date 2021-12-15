def count_words(text):
    return len(text.split(' '))

def count_upper_letters(text):
    result = 0
    for char in text:
        if char.isupper():
          result += 1
    return result

if __name__ == '__main__':
    teste_strings = "Uto Vvaiel Estouaqui"
    print (count_words(teste_strings))
    print (count_upper_letters(teste_strings))