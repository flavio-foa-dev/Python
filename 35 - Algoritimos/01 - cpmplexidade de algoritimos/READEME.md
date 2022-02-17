# Complexidade de algoritimos

### Vamos aprendere

  QUÃO EFICIENTE É ESSE ALGORITIMOS

Essa pergunta ja deve ter passado pela sua cabeça em varios momentos, quanto fazemos um site, por exemplo, nao queremos que ele seja lento; queremos um site que carregue rápido e responda rápido aos nossos comandos. Queremos uma API que não demore no tempo de resposta. E é super irritante quando abrimos um programa que deixa todo o nosso computador lento em função da quantidade de recursos que consome.
Pois bem! Hoje vamos aprender uma métrica universal para calcular o quão eficiente o seu algoritmo é! Funciona para qualquer linguagem e paradigma de programação e servirá de base para suas avaliações de eficiência daqui em diante.


### Seremos capazes de :
Descrever a capacidade de analisar o desempenho de um algoritmo como importante para processos seletivos de Big Techs, como Google, Amazon, Facebook, etc
Definir Ordem de Complexidade , ou Complexidade Assintótica , de como o quanto que o tempo de execução do algoritmo varia na medida em que a entrada cresce
Descrever a Ordem de Complexidade como definida com o uso de funções matemáticas que representam a proporção com que a grandeza mensurada cresce na medida em que o dado entrado cresce
Definir como O(1) a notação que representa um algoritmo de complexidade constante, ou seja, que não aumenta na medida em que o tamanho da entrada aumenta
Definir como O(n) a notação que representa um algoritmo de complexidade linear, ou seja, uma que reduz pela metade o tamanho do input a cada iteração
Definir como O(log n) a notação que representa um algoritmo de complexidade logaritmica
Definir como O(n^2) a notação que representa um algoritmo de complexidade quadrática
Definir como O(n^3) a notação que representa um algoritmo de complexidade cúbica
Definir Complexidade de Tempo como a métrica associada ao tempo que um algoritmo vai demorar para executar
Definir Complexidade de Espaço como a métrica associada ao espaço em memória que um algoritmo vai ocupar
Definir como O(2^n) a notação que representa um algoritmo de complexidade exponencial
Definir como O(n!) a notação que representa um algoritmo de complexidade fatorial
Definir o Problema do Caixeiro Viajante - Dada uma lista de cidade e a distância entre cada par de cidades, qual é a rota mais curta possível que visita todas as cidades exatamente uma vez e volta para a cidade de origem?
Definir a Categoria de Problemas NP-Completo como o conjunto de problemas que não tem solução conhecida em tempo polinomial, ou seja, que são fatoriais ou exponenciais
Combinar funções matemáticas para analisar complexidade de algoritmos - por exemplo, O( 3 log n), O (n log n), O(n^3 + n^2), que se simplifica como O(n^3)
Definir o Melhor caso de uma Ordem de Complexidade como o cenário com a entrada cujo processamento é feito, proporcionalmente, na menor quantidade de passos possível
Definir o Pior caso de uma Ordem de Complexidade como o cenário com a entrada cujo processamento é feito, proporcionalmente, na maior quantidade de passos possível
Definir o Caso médio de uma Ordem de Complexidade como o cenário de número de execução de passos que irá ocorrer para a maior parte de entradas possível

## Por que isso é importante

Para qualquer função com um valor de entrada pequeno , não damos importância à eficiência de um algoritmo. Vai ser rápido e pronto. Agora, e quando sua função tem que lidar com mil valores ao mesmo tempo? E cinco mil? E vinte mil? Quem sabe milhões de valores? Aí a eficiência do que você está fazendo começa a virar um problema. E nós precisamos ser capazes de lidar com cenários assim!
Acha esses valores exagerados? Pois exemplos não faltam! O famoso Discord , por exemplo, já encarou a demanda de ordenar alfabéticamente uma lista de amigos com até 250.000 pessoas. O tempo máximo que o algoritmo tinha pra rodar? Menos de um segundo e meio. E aí? Vai encarar?! (Se sua curiosidade despertou, busque o artigo nos recursos adicionais desse conteúdo depois que terminar seus estudos!)
As famosas Big Techs, por exemplo (Google, Amazon, Facebook, etc), fazem processos seletivos onde a capacidade de fazer esse tipo de análise é obrigatória. Em suma: quando sua escala fica grande, esse conhecimento se torna essencial. E com esse conhecimento você vai perceber que existem certos tipos de problemas que são irresolvíveis mesmo que você junte toda a capacidade computacional do planeta e trabalhe nele em potência máxima pelos próximos dez mil anos.
Acha exagero? Não é. 🙂

## Conteudo

Oberserve o algoritimo abaixo
```
def sum_array(numbers):
    sum = 0
    for number in numbers:
            sum += number

    return sum
```

Quanto tempo ele vai demorar para executar? 😁
"Ora, impossível dizer!", diz a pessoa incrédula. Depende da máquina, do que está rodando nela, dos recursos, de tudo! Não dá pra dizer.
Ok. Trave todas as configurações. É uma máquina padronizada, sem mais nada rodando, tudo certo. Quanto tempo ele vai demorar para executar? Um segundo? Dez segundos?
... Tem mais um "depende" aqui, não tem? O tempo de execução depende do tamanho do array passado por parâmetro! Quanto maior o dado passado por parâmetro, mais o algoritmo demorará para executar .
Hmmm. Legal! Vamos usar isso então! Eu não sei quanto tempo o algoritmo vai demorar para executar: dependem de inúmeros fatores além do meu controle. Mas uma coisa eu tenho certeza: o tempo de execução dele é proporcional ao tamanho do meu dado entrado! Por exemplo:

```
# def sum_array(numbers):
  # ...

# Suponha que, para o array abaixo, o tempo de execução seja `n`
sum_array(array_com_dez_mil_numeros)

# Nesse caso, aqui o tempo de execução vai ser `10 * n`, ou `10n`, já que o array é dez vezes maior que o anterior!
sum_array(array_com_cem_mil_numeros)

# Já esse é dez mil vezes maior que o primeiro, então esse aqui executa em `100n`
sum_array(array_com_um_milhão_de_numeros)
```
Pois bem!! A todas e a todos eu tenho o orgulho de apresentar a Ordem de Complexidade ! Mas o que raios é isso?! É o quanto que o tempo de execução do algoritmo varia na medida em que a entrada cresce! Observe:

```
# def sum_array(numbers):
  # ...

sum_array(array_com_dez_mil_numeros)
# O tempo de execução deste algoritmo foi 0.0004s

sum_array(array_com_cem_mil_numeros)
# Para uma execução com dez vezes mais números, o tempo aumentou em dez vezes: 0.004s

sum_array(array_com_um_milhão_de_numeros)
# Multiplicando o tamanho da entrada por dez novamente, temos um tempo dez vezes maior: 0.05s
```
Faça o teste na sua máquina (você já tem os conhecimentos para descobrir como fazer um script que mede esses tempos 🚀). Os valores podem variar, mas as proporções não! Um aumento no tamanho da entrada aumenta o tempo de execução na mesma proporção. Se fizéssemos um gráfico disso, ele seria assim:


A Ordem de Complexidade nada mais é do que a representação dessa proporção! Dado que o algoritmo é linearmente proporcional ao tempo de execução (ou seja, se a entrada aumenta em 10 vezes o tempo de execução também aumenta em 10 vezes), dizemos que este é um algoritmo linear!
A função matemática que representa uma relação linear é f(n) = n . Na notação de Ordem de Complexidade, dizemos que esse algoritmo é O(n) ! Guardem essa notação, vamos usá-la bastante!
💡 A Ordem de Complexidade pode ser chamada, também, de Complexidade Assintótica.

### Complexidade de tempo e de espaço
Vamos a um outro exemplo

```
def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
            array_of_squares.append(number * number)

    return array_of_squares
```
Para o algoritmo acima, aumentar a entrada em dez vezes aumenta em dez vezes o tempo de execução! A sua ordem de complexidade, portanto, é O(n) . Na maior parte das vezes em que falarmos de Ordem de Complexidade, estamos falando disso: do tempo que o algoritmo vai demorar para executar, ou complexidade de tempo . Há também uma outra complexidade: a complexidade de espaço , se referindo ao espaço em memória que o algoritmo ocupa.
A ideia é a mesma: na medida em que a entrada aumenta, quanto o espaço em memória usado pelo algoritmo aumenta? No exemplo acima, o algoritmo povoa e retorna um array de tamanho n , sendo n o tamanho do array entrado, e o retorna. Assim sendo, sua complexidade de espaço é O(n) !
💡 Se falamos em Ordem de Complexidade sem especificar se é de tempo ou de memória, assuma que é de tempo!
Mas e o outro exemplo, o do algoritmo sum_array() ?! Nesse caso, ele só precisa do espaço, em memória, de um número para executar. Para qualquer tamanho de entrada ele ocupa a mesma quantidade de espaço para executar. Assim sendo, sua complexidade de espaço é constante . Uma complexidade, seja de memória ou de tempo, ser constante, significa que o tamanho da entrada não influi no tempo de execução/memória ocupada de um algoritmo. A notação para esta complexidade é O(1)
💡 Quando calculamos a complexidade de espaço não levamos em consideração o espaço ocupado pela entrada! O tamanho da entrada não é algo que podemos, com nosso algoritmo, influenciar, então ele não entra em nossos cálculos.
Para fixar um pouco, vamos fazer um exercício!
Exercícios de Fixação
Exercício 1: Qual a Ordem de Complexidade (complexidade de tempo) do algoritmo abaixo? E a complexidade de espaço?

```
def multiply_array(numbers):
    result = 0
    for number in numbers:
            result *= number

    return result
```

### Complexidade Quadratica
Observe o algoritimo abaixo:

```
# Os arrays tem sempre o mesmo tamanho
def multiply_arrays(array1, array2):
    result = []
    for number1 in array1:
        for number2 in array2:
            result.append(number1 + number2)

    return result
```
Seus tempos de execução para um par de arrays de 2000 e 4000 elementos são:

```
# def multiply_array(numbers):
  # ...

sum_array(array_com_dois_mil_numeros)
# O tempo de execução deste algoritmo foi 0.45s

sum_array(array_com_quatro_mil_numeros)
# Já esse teve tempo de execução de 1.8s, cerca de quatro vezes maior.
```

Porque, dessa vez, quando dobramos o tamanho da entrada (de 2000 para 4000) nós quadruplicamos o tempo de execução? Ora, vejamos! Temos dois arrays do mesmo tamanho, que vamos chamar de n . Repare que temos dois loops aninhados um dentro do outro. Isso significa que, para cada número de array1 , todo o array2 será percorrido! Rode o exemplo abaixo para conferir:

```
def multiply_arrays(array1, array2):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f'Array 1: {number1}')
        for number2 in array2:
            print(f'Array 2: {number2}')
            result.append(number1 * number2)
            number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return result


meu_array = [1,2,3,4,5]

multiply_arrays(meu_array, meu_array)
```
Repare como, para dois arrays de tamanho 5, temos 25 iterações! Varie os números e veja como, sempre o número de iterações é n vezes n , ou seja, n² ! Por isso, lá em cima, multiplicar por dois o tamanho da entrada, de 2000 para 4000, multiplicou por quatro o tempo de execução: para um algoritmo O(n²) , aumentar a entrada em n vezes, aumenta o tempo de execução em n² vezes!
Para fixar um pouco, vamos fazer uns exercícios:

Exercício 2: Para desembaraçar a sopa de letrinhas que a seção anterior criou, meça o tempo de execução do algoritmo acima e, mudando o tamanho das entradas, veja como, se você aumenta a entrada em n vezes, o tempo de execução aumenta em n² vezes!
Exercício 3: Faça um algoritmo qualquer com três loops aninhados um dentro do outro. Entenda como ele terá uma complexidade de O(n³) !
Se tiver dificuldades, nos procure!
