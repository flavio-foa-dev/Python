### Entrada e saida em python
### O que vamos aprender ?
Hoje, vamos aprender a estruturar um projeto Python, adicionando  um novo elemento aos nossos programas. Aprederemos como adicionar entrada e saida  de dados e manipular  alguns tipos de arquivos, como csv e json.  Assim poderemos persistir dados.

**Você sera capaz de:**
 - Preparar um ambiente de projeto em Python, definido sua  estrutura de diretórios  e criando ambiente isolados;
 - Instalar bibliotecas de terceiros num projeto Python;
 - Entender como lidar com exceções em python;
 - Receber dados de pessoas usuarias, assim como envialas de volta;
 - Ler e escrever arquivos no formato tabular `csv` === "separados por vigulas"
 - Serializar e dessearalizar dados no formato `Json`

### Isso é importante para

No dia a dia, podemos encontrar aplicações grandes e complexas, que necessitam de uma estruturação do codigo-fonte. A fim de facilitar a manutenção, é uma boa pratica dividir um programa em arquivos menores. por esse motivo, é importante entender o que são **Modulos e pacotes** e como eles funcionam em uma aplicação

Já os dados, são  uma das coisas mais valiosas para uma empresa, porque  podemos se torna informação. A análise desses dados é cada vez mais decisiva para o sucesso ou fracasso de um negocio. A tomada de decisão pode se embasar em informações relevantes como, por exemplo, o nivel do cliente(CSAT)e o seu custo de aquisição para a empresa(CAC)

Aprendendo a manipular arquivos, poderemos persistir dados, recuperá-los e analisá-los posteriormente. Quando dizemos que vamos persistir dados, significa que iremos armazenar/salvar os dados para serem recuperados quando necessários no futuro.
Vivemos em um mar de informações. Porém afogados na ignorância.
Além disso, integração entre sistemas é algo que uma pessoa programadora provavelmente vai se deparar em algum momento de sua carreira. Por isso, é importante conhecer formatos como o JSON , largamente utilizado para comunicação entre sistemas, e o CSV , amplamente utilizado no contexto da Ciência de Dados

### Estruturando uma aplicação
 - Modulos

Um **modulo* é um arquivo que contem definições e instruções em python. O nome do arquivo é um nome acrescido de `.py.` Dentro de um arquivo python, você pode importa um modulo e ter acesso as suas funçõe e classes, etc.

Em linhas gerais, todo arquivo que é escrito com a linguagem python e com a extenção .py é considerado um modulo.
Observe o arquivo `my_math.py`

```
def sum(a, b):
  return a + b


def pot(a, b):
  return a ** b


print(sum(2, 2))
print(pot(2, 3))
```
Este arquivo é um modulo python, que pode ser executado como scripts, com o comando `python3 my_math_py`. se isso ocorre, o retorno será, em ordem, 4 e 8, devido as chamadas das funções dentro dos metodos `print()`.
Etretanto as funções que criamos neste podem ser reaproveitadas por outros módulos, atraves da declaração`import`
A medida que fomos avançando, esses conceitos ficarão cada vez mais claros.

Pacotes 📦

Pacotes são módulos Python que contêm outros módulos e/ou pacotes , comumente separados por responsabilidades similares. Na prática, um pacote é um diretório que pode conter vários módulos (arquivos de extensão .py ) e/ou outros pacotes .
Exemplo de tipos diferentes de imports de pacotes :

```
import http  # importa o pacote http como um módulo

from http import client  # importa o módulo client do pacote http

from http.client import HTTP_PORT  # importa a constante HTTP_POST do módulo client do pacote http
```
tudo isso ficara mais perceptivel, a medida que fomos avançando no conteudo.

### Ambiente virtual

Imagine que , em uma maquina, ha um projeto Python que tem alguns pacotes de terceiros instalados e, dentre eles, ha uma biblioteca na versão 14. imagine também que, na mesma maquina, um novo projeto é iniciado e ele precisa de mesma biblioteca, mais desta vez 2.0 o que fazer? As versçoes são compativeis? se eu atualizar o sistema, a versão antiga vai continuar a funcionar?

O `Venv` entra como resposta a essas perguntas! Ele é um modulo, ja embutido na linguagem, que serve para isolar ambientes entre projetos, Ou seja, eu consigo ter doiius projetos rodando, em dois ambientes diferentes, com versões diferentes de uma mesma biblioteca.

Na pratica, o que vamos fazer é instalar as bibliotecas em um diretório, que esta relacionado ao projeto. Assim, cada projeto pode ter suas propias bibliotecas na versões que quiser. A idéia é a mesma do `npm` no nodeJs

O comando para criação deste ambiente isolado é `python3 -m venv .venv`, sendo que o `.venv` é o nome do ambiente isolado. Este comando deve ser executado na raiz do projeto.

💡 Caso o venv não esteja instalado, utilize o comando `sudo apt install python3-venv `.

Este ambiente isolado será visto como um diretório criado na raiz do projeto. O ponto na frente do nome faz com que o diretório fique oculto.
Depois de criado, temos de ativar este ambiente para usá-lo. Isto é importante, pois sempre que decidirmos trabalhar neste projeto devemos repetir este passo.

 ```
 source .venv/bin/activate
 ```
 Você pode conferir se o comando de ativação do ambiente virtual deu certo com o seguinte comando:
 ```
 which python3
 ```
O resultado será o caminho para a pasta onde você criou seu ambiente virtual ( pwd ), acrescido de .venv/bin/python3 .
Pronto, agora estamos preparados e preparadas para instalar as bibliotecas que precisaremos para nossos projetos.

### Entrada e Saída
De modo geral, podemos dizer que um programa seria menos útil se não pudéssemos coletar valores de pessoas usuárias e muito menos agradável de se utilizar caso o resultado apresentado fosse pouco legível.
Existem algumas maneiras de nos comunicarmos com o exterior do programa em Python para recebermos dados, assim como existem maneiras de melhorar a exibição dos nossos resultados.

### O que vamos aprender
Heje, vamos aprender a estruturar  um projeto Python, adicionando tambem um novo  elemento aos nossos programas . Aprederemos como adicionar entrada e saida de dados e a manipular alguns tipos de arquivos CSV e Json. Assim, poderemos persistir dados.

### Sera capaz de :
- preparar um ambinete em Python, definindo sua estrutura de diretórios e criando ambientes isolados;
- Instalar biblioteca de terceiros num projeto python para
- Entender como lidar com exceções em Python;
- Receber dados de pessoas usuarias, assim como envia-los de volta;
- Ler e escrever arquivos no formato tabular `csv`;
- Serializar e dessearalizar dados no formato `Json`.

### Isso é importante.
No dia a dia, poderemos encontrar aplicações grandes e complexas, que necessitam de uma melhor estruturação do código-fonte. A fim de facilitar a manutenção, é uma boa prática dividir um programa em arquivos menores. Por esse motivo, é importante entender o que são módulos e pacotes e como eles funcionam em uma aplicação.
Já os dados, são uma das coisas mais valiosas para uma empresa, porque podem se tornar informação. A análise desses dados é cada vez mais decisiva para o sucesso ou fracasso de um negócio. A tomada de decisão pode se embasar em informações relevantes como, por exemplo, o nível de satisfação do cliente (CSAT) e o seu custo de aquisição para a empresa (CAC).
Aprendendo a manipular arquivos, poderemos persistir dados, recuperá-los e analisá-los posteriormente. Quando dizemos que vamos persistir dados, significa que iremos armazenar/salvar os dados para serem recuperados quando necessários no futuro.
Vivemos em um mar de informações. Porém afogados na ignorância.

### Entrada e Saída
Funções podem receber argumentos das pessoas que usam o programa, processá-los e retornar algum valor. Mas como estes argumentos chegam a elas? E o resultado do nosso processamento, como exibi-lo para a pessoa utilizando nossa aplicação?
De modo geral, podemos dizer que um programa seria menos útil se não pudéssemos coletar valores de pessoas usuárias e muito menos agradável de se utilizar caso o resultado apresentado fosse pouco legível.
Existem algumas maneiras de nos comunicarmos com o exterior do programa em Python para recebermos dados, assim como existem maneiras de melhorar a exibição dos nossos resultados.

### Entrada

Uma das maneiras que existem de receber valores em nossos programas é  através  da função `ìmput`, que vem embutida na propia linguagem. Esta função esta vinculada a entrada padão do sistema operacional e tem como paramentro opcional o `prompt` que, caso seja fornecido, exibira a mensagem passada  para ele em tela. O valor recebido atraves da função será do tipo texto(`str`):

```
input("Digite uma mensagem:")
```
O programa permanece parado até  que algum dado seja forneciso. isto pode ser feito digitando algum conteudo, teclando `enter` ou podemos tambem ter os dados redirecionados de um arquivo ou outra fonte. Veja um exemplo de um programa com entrada  de dados fornecido pela usuária:

```
import random

random_number = random.randint(1, 10)  # escolhe um número aleatório entre 1 e 10
guess = ""

while guess != random_number:  # enquanto não adivinhar o número
    guess = int(input("Qual o seu palpite? "))  # pergunte a pessoa usuária um número

print("O número sorteado era: ", guess)
```
💡 Fazemos uma conversão do palpite para um número inteiro, pois entrada de dados é sempre str .
💡 Para rodar o exemplo  acima, não crie um arquivo chamado `random` para inserir o código, pois o módulo que estamos importando se chama `random`, e isso pode ocasionar  num erro! Lembre-se que, para rodar o código, você deve executar, no terminal, o comando `python3 nome_do_arquivo.py`

Outra maneira de recebermos  valores externos na execução de nossos programas é utilizando o `modulo sys`. quando executamos um scripts e adicionamos parâmetros, os mesmos estarão disponiveis atrave is de uma variavel chamada `sys.argv` que é preenchida sem que precisamos fazer nada. Na pretica. podemos escrever o conteudo abaixo em um arquivo e, ao executarmos, passamos alguns parâmetros:

```
import sys


if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)
```
Para executarmos passando os parâmetros utilizaremos o comando

```
 python3 arquivo.py 2 4 "teste"

Received ->  arquivo.py
Received ->  2
Received ->  4
Received ->  teste

```
### Saída

Como ja visto a função `print`, que ja vem embutida na liguagem, é a principal função para imprimirmos um valor em "tela", Normalmente esta função escreve na saida padrão do sitema operacional, mas iremos ver que podemos modificar este e outros comportamentos.

Esta função recebe parâmetros de forma variavel, ou seja pode receber nenhum, um, dois ou n pârametros durante sua invocação

```
print("O resultado é", 42)  # saída: O resultado é 42
print("Os resultado são", 6, 23, 42)  # saída: Os resultados são 6 23 42
```
Podemos Alterar o separador dos argumentos passados, que por padão, é um espaço em branco.

```
print("Maria", "João", "Miguel", "Ana")  # saída: Maria João Miguel Ana
print("Maria", "João", "Miguel", "Ana", sep=", ")  # saída: Maria, João, Miguel, Ana
```
Alem do separador, podemos tabem alterar o caracter de fim de linha que , por regra, é uma quebra de linha:

```
print("Em duas ")
print("linhas.")
```
Saída

```
Em duas
linhas.
```
uma diferença de parametros
```
print("Na mesma", end="")
print("linha.")
```
```
Na mesma linha.
```
Já sabemos que erros podem acontecer, e o sistema operacional normalmente espera que um programa escreva seus erros na saida de erros.
Existe um parametro que nos permite modificar a saida padrão para  a saida de erros

```
import sys

err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr)
```

💡 Em Python , podemos fazer interpolação de variáveis e expressões utilizando f-string . Adicionamos um f antes das aspas e o valor de saída entre chaves. Essa dica é importante, pois é a maneira mais eficiente de formatar strings.

```
x = 5
y = 3
print(f"{x} / {y} = {x / y:.2f}")  # saída: 5 / 2 = 1.67
# {x} é substituído por 5
# {y} é substituído por 3
# {x / y:.2f} O que vem após os dois pontos são formatadores, como nesse exemplo, duas casas decimais (.2f).
print(f"{x:.^3}")  # saída: ".5."
# . é o caractere utilizado para preencher
# ^ indica que o valor será centralizado
# 3 são o número de caracteres exibidos
```

### Manipulação de arquivos

seja para armazenar algumas informação processada ou para manipular imagens, audios, videos ou recuperar dados de uma planilha, precisamos fazer a manipulação de arquivos.
Podemos fazer uma operação de leitura, de escrita ou ate de ambas, a depender da nossa necessidade. porem idepedentemente da operação executada, é preciso sempre fechar o arquivo apos operá-lo

A função `open` é respomsavel por abrir um arquivo, tomando possivel sua manipulação. Seu único parâmetro obrigatório é o nome do arquivo. Por padão. arquivo são abertos somente para leitura, mas podemos modificar isto passando o modo como vamos abrir o arquivo . No exemplo abaixo , estamos utilizando `mode="w"`. ou seja , estamos abrindo o arquivo para escrita.

```
file = open("arquivo.txt", mode="w")  # ao abrir um arquivo para escrita, um novo arquivo é criado mesmo que ele já exista, sobrescrevendo o antigo.
```
Para escrevermos um conteúdo em um arquivo utilizamos a função write :
```
# file = open("arquivo.txt", mode="w")

file.write("nome idade\n")
file.write("Maria 45\n")
file.write("Miguel 33\n")
```
💡 Podemos escrever em um arquivo apenas após abrirmos ele.

Assim como podemos redirecionar a saída do nosso programa para saida de erros, podemos fazer o mesmo redirecionando o conteudo digitado dentro de `print` para arquivo. Ou seja, tambem podemos escrever em uma arquivo através do `print`

```
#
# file.write("Miguel 33\n")


# Não precisa da quebra de linha, pois esse é um comportamento padrão do print
print("Túlio 22", file=file)
```

Para escrever multiplas  linhas podemos utilizar a função `writelines. Repare que a função espera que cada linha tenha seu propio caractere de separação (\n):

```#
# print("Túlio 22", file=file)


LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
file.writelines(LINES)
```
Abrimos o arquivo, escrevemos seu conteudo, vamos então fechalo:

```
# file.writelines(LINES)


file.close()
```
Mas por que devemos sempre fechar um arquivo? A resposta vem do sistema operacional. Temos um limite de quatos arquivos podemos abrir de uma so vez, e um erro é lançado quando atigimos esse limite. Vamos ver um codigo para desmonstrar a ocorrencia de um erro ao abrir muitos arquivos ao mesmo tempo:

```
arquivos = []
for index in range(10240):
    arquivos.append(open(f"arquivo{index}.txt", "w"))
```
O numero que o programa ira falhar pode variar, pois o sistema operacional manntém alguns arquivos abertos para seu propio uso.
outro motivo importante para se fechar os arquivos é que normalmente a manipulação de arquivos é feita através de buffers. Ou seja, a escrita em disco pode não ser imediata. quando fechamos o arquivo, Garantimos que tudo aquilo que ainda não esta escrito seja persistido.

A Leitura do conteúdo de um arquivo pode ser feita utilizando a função `read`. Para experimentar, vamos escrever em um arquivo e lê-lo logo em seguida!

```
# escrita
file = open("arquivo.txt", mode="w")
file.write("Trybe S2")
file.close()

# leitura
file = open("arquivo.txt", mode="r")
content = file.read()
print(content)
file.close()  # não podemos esquecer de fechar o arquivo
```
Um arquivo é tambem um iterável, ou seja, pode ser percorrido em um laço de repetição.AA cada iteração, uma nova linha ṕe retornada. Vamos fazer igual ao exemplo anterior, porem dessa vez vamos escrever mais de uma linha!
```
# escrita
file = open("arquivo.txt", mode="w")
LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
file.writelines(LINES)
file.close()

# leitura
file = open("arquivo.txt", mode="r")
for line in file:
    print(line)  # não esqueça que a quebra de linha também é um caractere da linha
file.close()  # não podemos esquecer de fechar o arquivo
```
