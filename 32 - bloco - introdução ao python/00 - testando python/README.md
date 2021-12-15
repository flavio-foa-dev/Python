# Python
sistemas em python

difine
dif

 Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

- `python3 -m pip install -r dev-requirements.txt`

3//2 = 1
3/2 = 1.5
5%2 = 1

|| = or
&& = and

int = inteiro
float =  ponto flutuante
str = String
bool = booleanos

list = array
.append('nome') = adiona novo elemento a list
.remove('nome') = remove elemento na list
.extend(nome list) = junta duas list

tupla = conjunto numero qualquer de elementos   === objeto no javascripts

great_chess.extend(
    [
        (great_chess[2], 18),
        (great_chess[3], 15),
        (great_chess[4], 21),
    ]
)

dicionario === seria objeto com os nomes da propiedades
{"nome": "Flavio",}

conjunto {'alberto', 'gabi'}
conjunto1 {'alberto', 'luka'}
conjunto.intersection(conjunto1)
// retorna o que os dois conjuntos tem em comum .
conjunto.difference(conjunto')
// retorna os elementos diferentes

conjunto.union(conjunto1)
// unifica os dois conjuntos

lista === um lista de entidades
tupla === um unica entidade com seus atributos
dicionario === quando queremos associar chave e valor

fruits = ["orange", "apple", "grape", "pineapple"]  # elementos são definidos separados por vírgula, envolvidos por colchetes

fruits[0]  # o acesso é feito por indices iniciados em 0

fruits[-1]  # o acesso também pode ser negativo

fruits.append("banana")  # adicionando uma nova fruta

fruits.remove("pineapple")  # removendo uma fruta

fruits.extend(["pear", "melon", "kiwi"])  # acrescenta uma lista de frutas a lista original

fruits.index("apple")  # retorna o índice onde a fruta está localizada, neste caso 1
 em seu programa
fruits.sort()  # ordena a lista de frutas

 O método type(operando) corresponde ao operador typeof operando do JavaScript.

 permissions = {"member", "group"}  # elementos separados por vírgula, envolvidos por chaves

permissions.add("root")  # adiciona um novo elemento ao conjunto

permissions.add("member")  # como o elemento já existe, nenhum novo item é adicionado ao conjunto

permissions.union({"user"})  # retorna um conjunto resultado da união

permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

Conjuntos imutáveis (frozenset)
Variação do set, porém imutável, ou seja, seus elementos não podem ser modificados durante a execução do programa.
Sintaxe:
permissions = frozenset(["member", "group"])  # assim como o set, qualquer estrutura iterável pode ser utilizada para criar um frozenset

permissions.union({"user"})  # novos conjuntos imutáveis podem ser criados à partir do original, mas o mesmo não pode ser modificado

permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

Dicionários (dict)
Estrutura que associa uma chave a um determinado valor. É a representação do tão famoso objeto que utilizamos em JavaScript.
Sintaxe:
people_by_id = {1: "Cássio", 2: "João", 3: "Felipe"}  # elementos no formato "chave: valor" separados por vírgula, envolvidos por chaves

people_by_name = {"Cássio": 1, "João": 2, "Felipe": 3}  # outro exemplo, dessa vez usando strings como chaves (ao contrário de JS, as aspas duplas são obrigatórias)

# elementos são acessados por suas chaves
people_by_id[1]  # saída: Cássio

# elementos podem ser removidos com a palavra chave del
del people_by_id[1]
people_by_id.items()  # dict_items([(1, "Cássio"), (2, "João"), (3, "Felipe")])
# um conjunto é retornado com tuplas contendo chaves e valores
Em JavaScript, não precisávamos colocar a chave do objeto entre aspas, porém, em Python, isso é necessário.

Range (range)
Estrutura capaz de gerar uma sequência numérica de um valor inicial até um valor final, modificando seu valor de acordo com o passo ( step ) definido. Pode ser declarado como range( [start], stop[, step] ) , em que start e step podem ser omitidos, possuindo valores iniciais iguais a 0 e 1 respectivamente.
Um ponto de atenção é que o stop não é incluído na sequência, portanto caso queira uma sequência de 1 até 10 a chamada deverá ser range(1, 11)
Seus valores são criados a medida que esta sequência é percorrida.
Sintaxe:

# vamos converter o range em uma lista para ajudar na visualização

# definimos somente o valor de parada
list(range(5))  # saída: [0, 1, 2, 3, 4]

# definimos o valor inicial e o de parada
list(range(1, 6))  # saída: [1, 2, 3, 4, 5]

# definimos valor inicial, de parada e modificamos o passo para 2
list(range(1, 11, 2))  # saída: [1, 3, ,5 ,7 , 9]

# podemos utilizar valores negativos para as entradas também
list(range(10, 0, -1))  # saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

### bibliotecas no python
no pytho voce so importa  diferente do java scripts que voce estala via npm install "nome"
sintaxe
from random import randint

for good in list_array:
    domminios.append(god["dominio"])

key = "id"
from_to = {
    "id": "identifier",
    "mail": "email",
    "lastName": "last_name",
}
from_to[key]