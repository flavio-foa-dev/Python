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
Alem de arquivos textuais como os que manipulamos até agora, temos tambem arquivos binarios. Eles são arquivos que contêm uma serie de bytes e a sua leitura pode variar  de acordo co o arquivo. Nesse caso, devemos acrescentar um `b` ao paramentro `mode`
As operações São similares a de um arquivo textual. porem tanto a escrita quanto a leitura devem ser feitas utilizando bytes

```
# escrita
file = open("arquivo.dat", mode="wb")
file.write(b"C\xc3\xa1ssio 30")  # o prefixo b em uma string indica que seu valor está codificado em bytes
file.close()

# leitura
file = open("arquivo.dat", mode="rb")
content = file.read()
print(content)  # saída: b'C\xc3\xa1ssio 30'
file.close()  # não podemos esquecer de fechar o arquivo
```
Erros podem acontecer, um arquivo pode não existir, permissões podem faltar e codificações podem falhar. Por isso, temos de garantir que, um erro ocorro, ainda assim faremos o fechamento do nosso arquivo. Como conseguimos lidar com erro em Python? Vamos agora falar sobre exceções!

## Lidando com exceções
Há pelo menos dois tipos de erros podem ser destacados: erris de sintaxe e exceções.

## Erros de sintaxe
Como nos bem sabemos, erros de sintaxe ocorrem quando o codigo utiliza recursos inexistentes da linguagem, que  não consegue  interpreta-lo. É como executar `print{"ola,mundo!"} em vez de print("ola, mundo!")`

## exceções
Ja as exceções, ocorrem durante a execução e acabam resultando em mensagem de erro. Veja exemplos de exceções:

```
print(10 * (1 / 0))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
print(4 + spam * 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
print('2' + 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
Observe que, apenas no exemploacima, podemos observar três exceções
`ZeroDivisionError , NameError e TypeError`. a lista completa de exceções ja embutidas na linguagem

### Tratamento de exceções
Para psrs tratamento exceções, utilizamos o conjunto de instruções `try`, com palavras reservadas `try`e `except` O funcionamneto dessa clausula da seguinte forma:

- se nenhum exceçãos ocorrer, a clausula `except` é ignorada, e a execução da instrução `try` é finalizada.
- se ocorrer uma exceção durante a execução da clausula `try`, as instruções remanescente na clausula são ignoradas. se o tipo da exceção ocorrida tiver sido previsto em algum `except`, então essa clausula será executada.
- se não existir nenhum tratador previsto para tal exceção. trata- se de uma exceção nao tratada e a execução do programa termina com uma msg de error.

exemplos
```
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```

Cole o código acima no terminal interativo e teste, na prática, como funciona o tratamento de exceções.

## Lidando com exceções  enquanto manipula arquivos
Agora cientes de como tartar exceções, podemos nos previnir de possiveis erros que ocorrem quando manipulamos arquivos. Sempre devemos fechar um arquivo e podemos, em um bloco `try`, fazer isso utilizando a instrução `finally ou else`  O `finally` e uma outra clasula do conjunto `try`, cuja finalidade e permitir a implementação de ações de limpeza, que sempre devem ser executadas idepedentemente da ocorrencia de ações. Já o else ocorre sempre que todo o try for bem sucedido.

```
try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")
```
Como estamos abrindo o arquivo em modeo leitura, caso ele não exista , uma exceção sera levantada, executando as clausulas `exception` e `finally`. Etretando se alterarmos o modo para escrita, o arquivo sera criado mesmo se inesxixtente, executando as clausulas `else` e `finally`.

Este padão e tão comum, não so em arquivos como em outros recursos que devemos utilizar e liberar ao final, como conexão de banco de dados, por exemplo, que o Python tem um mecanismo propio para lidar com isto.

o `with` é  a palavra reservada paara gerenciamento de contexto. Este gerenciamento (`with`) é utilizado para encapsular a utilização de um rercuso, garantindo que certas ações sejan tomadas indepedentemente  se ocorreu ou não um erro naquele contexto.

A função `open` retorna um objeto que se comporta como um gerenciador de contexto de arquivos que sera responsavel por abrir e fechar o memo. isto significa que o arquivo possui mecanismo especiais que, quando invocado, utilizando `with`, alocam um determinado recurso, no caso um arquivo, e, quando for terminado, este recurso será liberado.

```
# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
with open("arquivo.txt", "w") as file:
    file.write("Michelle 27\n")
# como estamos fora do contexto, o arquivo foi fechado
print(file.closed)
```
💡 Já vimos a utilização de gerenciadores de contexto em testes. Lá, capturamos exceções que ocorrem e verificamos se naquele contexto a exceção lançada era a esperada. Não há um recurso a ser liberado, mas estamos garantindo que uma asserção será feita naquele contexto.

### Manipulando arquivos JSON

JSON é um formato textual muito utilizado para ntegração de sistema. ELE  é baseado em um   subconjunto de regras JavaScript, embora seja  idepedente de linguagem.

Por sua legibilidade tamanha (è bem leve ), alem da facilidade de leitura e escrita por seres humanos, vem sendo  bastante utilizado na web e para troca de informações entre istemas.

Alguns exemplos de utillização incluem comunicação com o back-end e front-end, comunicação com o sistemas externos, como por exemplo gateway de pagamento, ou  tambem internos como um sistema de autenticação.
a linguagem Python ja inclui um modulo para manipulação desse tipo de arquivo e seu nome e json

Seus principais metodos para manipulação são: `load, loads, dump, dumps.`
🐭 Para demostrar de como é feita a manipulação de arquivos JSON, vamos utilizar um arquivo de exemplo, que é uma lista de objetos com suas informações em chave valor

```
import json  # json é um modulo que vem embutido, porém precisamos importá-lo


with open("pokemons.json") as file:
    content = file.read()  # leitura do arquivo
    pokemons = json.loads(content)["results"]  # o conteúdo é transformado em estrutura python equivalente, dicionário neste caso.
    # acessamos a chave results que é onde contém nossa lista de pokemons

print(pokemons[0])  # imprime o primeiro pokemon da lista
```
A leitura pode ser feita diretamente do arquivo, utilizando o método `load` ao invés de `loads` . O `loads` carrega o `JSON` a partir de um texto e o `load` carrega o `JSON` a partir de um arquivo.

```
import json


with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

print(pokemons[0])  # imprime o primeiro pokemon da lista
```
A escrita de aarquivos no formato `JSON` é similar a escrita de arquivos comum, porém primeiro temos de transformar  os dados.

```
import json

# Leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# Separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# Abre o arquivo para escrevermos apenas o pokemons do tipo grama
with open("grass_pokemons.json", "w") as file:
    json_to_write = json.dumps(
        grass_type_pokemons
    )  # conversão de Python para o formato json (str)
    file.write(json_to_write)
```
Assim como a desserialização,que faz a transformação de texto em formato **JSON** para **Python**, a serialização, que é o caminho inverso, tambem possui um metodo equivalente para escrever em arquivos de forma direta

```
import json

# leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# abre o arquivo para escrita
with open("grass_pokemons.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(grass_type_pokemons, file)
```
💡 Arquivos JSON não seguem a nomenclatura habitual de leitura e escrita ( write e read ), pois são considerados formatos de serialização de dados. Seguem então as mesmas nomenclaturas utilizadas em módulos como marshal e pickle , que também são formatos de serialização.

### Manipulando arquivos csv

O formato **CSV** ( Comma Separated Values ) é muito comum em exportação de planilhas de dados e base de dados. Foi utilizado por muito tempo antes de sua definição formal e isso acabou gerando uma não padronização neste formato e o surgimento de varios dialetos.

Cada dialeto tem seus própios delimitadores e caracteres de citação, porem o formato geral é semelhante o suficiente para utilizarmos o mesmo modulo para este processamneto.

Ainda que seu nome indique que o delimitador seja a `,` (Virgula), existe variações que utilizam `;` (ponto e virgula), ou até mesmo tabulação ("\t)

🎲 Sem dúvidas, analise de dados é o que se destaca quando estamos falando sobre manipular arquivos **CSV**. Vamos analisar então uma base de dados
 💡 Para fazer o exemplo, cole o arquivo balneabilidade.csv na raiz do diretório em que estará o seu script.

### o modulo CSV, contem  duas principais funções:

  - Um leitor (reader) que nos ajuda a ler o conteudo, ja fazendo as transformações dos valores para PYTHON;
  - e um escritor (write) para facilitar a escrita nesse formato.

```
import csv

with open("balneabilidade.csv") as file:
    beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = beach_status_reader

print(data)
```
O leitor define como dialeto padão `excel`, que significa dizer que i delimitador de campos sera a "," e o caractere de citação sera as aspas duplas("). Uma forma de modificar estes padões e definindo-os de forma diferente na criação do leitor.

Um jeito de **CSV** pode ser pecorrido utilizando o laço de repetição `for` e, a cada interação, retorna uma nova linha ja transformada em uma lista python com seus respectivos valores.
`header` `*data` é um truque para separarmos o cabeçalho do restante dos dados. quando ha uma atribuiçãomultipla e o valor da direita(`beach_status_reaader)"uma propiedade do arquivo csv". Pode ser pecorrido, o Python entende que deve atribuir  cada um dos valores  a uma variavel da esquerda  (header, *data), seguindo a ordem. Isto é chamdo de desempacotamento de valores. Dito isso, vamos ver o exemplo

 💡 Execute o código abaixo para que você veja os valores printados e entenda melhor o funcionamento.

```
a, b = "cd"
print(a)  # saída: c
print(b)  # saída: d

head, *tail = [1,2,3] # Quando um * está presente no desempacotamento, os valores são desempacotados em formato de lista.
print(head)  # saída: 1
print(tail)  # saída: [2, 3]
```
Podemos fazer uma analise agrupando a balneabilidade **por campanha** e depois salvando o resultado tambem no formato csv.

```
import csv

# lê os dados
with open("balneabilidade.csv") as file:
    beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = beach_status_reader

# agrupa campanhas e suas respectivas balneabilidades
bathing_by_campaign = {}
for row in data:
    campaign = row[6]
    bathing = row[2]
    if campaign not in bathing_by_campaign:
        bathing_by_campaign[campaign] = {
            "Própria": 0,
            "Imprópria": 0,
            "Muito Boa": 0,
            "Indisponível": 0,
            "Satisfatória": 0,
        }
    bathing_by_campaign[campaign][bathing] += 1

# escreve o relatório em csv
# abre um arquivo para escrita
with open("report_por_campanha.csv", "w") as file:
    writer = csv.writer(file)

    # escreve o cabeçalho
    headers = [
        "Campanha",
        "Própria",
        "Imprópria",
        "Muito Boa",
        "Indisponível",
        "Satisfatória",
    ]
    writer.writerow(headers)

    # escreve as linhas de dados
    for campaign, bathing in bathing_by_campaign.items():
        # desempacota os valores de balneabilidade para formar uma linha
        # equivalente a
        # row = [campaign]
        # for value in bathing.values():
        #     row.append(value)
        row = [campaign, *bathing.values()]
        writer.writerow(row)
```
Existe ainda o leitor e escritor baseado em dicionarios. Sua principal vantagens é que, com  ele , nao precisamos manipular os indices para acessar os dados das colunas. Mas, devido a estrutura de dados utilizada, ele tem como desvantagem o espaço ocupado em memoria, sendo maior que i comum:

```
import csv

# lê os dados
with open("balneabilidade.csv") as file:
    beach_status_reader = csv.DictReader(file, delimiter=",", quotechar='"')
    # a linha de cabeçaçhos é utilizada como chave do dicionário
    # agrupa campanhas e suas respectivas balneabilidades
    bathing_by_campaign = {}
    for row in beach_status_reader:
        campaign = row["numero_boletim"]  # as linhas são dicionários
        bathing = row["categoria"]
        if campaign not in bathing_by_campaign:
            bathing_by_campaign[campaign] = {
                "Própria": 0,
                "Imprópria": 0,
                "Muito Boa": 0,
                "Indisponível": 0,
                "Satisfatória": 0,
            }
        bathing_by_campaign[campaign][bathing] += 1

# abre um arquivo para escrita
with open("report_por_campanha_dicionarios.csv", "w") as file:
    # os valores a serem escritos devem ser dicionários
    header = [
        "Campanha",
        "Própria",
        "Imprópria",
        "Muito Boa",
        "Indisponível",
        "Satisfatória",
    ]
    # É necessário passar o arquivo e o cabeçalho
    writer = csv.DictWriter(file, fieldnames=header)
    # escreve as linhas de dados
    for campaign, bathing in bathing_by_campaign.items():
        # desempacota os valores de balneabilidade para formar uma linha
        # equivalente a
        # row = {"campanha": campaign}
        # for name, value in bathing.items():
        #     row[name] = value
        row = {"Campanha": campaign, **bathing}
        writer.writerow(row)
```
💡 Ainda que a manipulação de arquivos seja algo trivial, caso precise fazer análises de dados, leve em consideração bibliotecas como Pandas , elas foram construídas e são mantidas justamente para atender e facilitar este objetivo.