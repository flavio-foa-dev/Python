### o QUE SERA O ESTUDO

A rercursividade não esta presente apenas na area da computação, A recursividade também existe na filosofia, na matematica, e na linguagem. Mas Hoje, veremos especificamente a recursividadena  nossa  area , a da computação. Para aprender  recursividade você precisa aprender recursividade. 😂

Nesta aula vamos aprender o que é recursividade, como desenvolver algoritmos recursivos e quando utilizá-los.
Curiosidade: Pesquise "recursividade" no Google. 👀

# vamos estudar
- Entender o conceito recursividade;
- Analizar algoritimos recursivos
- Resolver problemas de forma recursiva

# Por que isso é importante?
A recursividade desenpenha um papel  central na programação funcional e na ciência da computação . No paradigma funcional, por exemplo, a recursividade é o mecanismo básico para repetições

Com a recursividade conseguimos solucionar alguns problemas de forma mais  simplificadae legante, diminuindo a complexidsade de escrita do codigo.

Normalmente a solução recursiva é adotada em situações onde o código fica menos complexo se comparado ao código da solução iterativa, para o mesmo problema. Ao utilizar a recursão não há nenhum benefício quanto ao desempenho do programa. A recursão é mais usada para tornar a resposta mais evidente.
"Os loops podem melhorar o desempenho do seu programa. A recursão melhora o desempenho do seu programador. Escolha o que for mais importante para a sua situação."
Muitos algoritmos importantes usam a recursão, então é fundamental aprendermos esse conceito.

# conteudo

# Entrevista Whiteboard: Fibonacci
Imagine que voce vai fazer uma entrevista para uma empresa onde voce sempre sonhou em trabalhar.Nocê vai fazer uma whiteboard interview, onde voce tem um tempo limitado para resolver um problema de programação; quem sabe faz ao vivo! veja o problema;
A  sequência de fibonacci é uma sequência numérica em que, partindo dos dois primeiros números sendo 0 e 1, o próximo número será sempre a soma dos dois anteriores. Esta sequência é interessante pois aparece muito na matemática e na natureza de formas inusitadas. Veja os primeiros números:

```
começo = [0, 1]
0 + 1 = 1 -> [0, 1, 1]
1 + 1 = 2 -> [0, 1, 1, 2]
1 + 2 = 3 -> [0, 1, 1, 2, 3]
3 + 2 = 5 -> [0, 1, 1, 2, 3, 5]
```
Assim por diante: 8, 13, 21, 33, 54 ....
Faça uma função que retortnr o enésimo numero da sequencia de fibonanci

# formas de resolver!

Ao tentar resolver este problema, uma coisa que deve ter notado é que, para saber um número qualquer da sequência é necessário saber os dois anteriores. (Exceto para os dois primeiros.) Por isso, para calcular o número N da sequência de fibonacci, sempre precisaremos calcular N-1 e N-2. Observe esta solução:

```
 def fibonacci_iter(n):
    sequence = [0, 1]
    if n >= 2:
        for x in range(2, n+1):
            next = sequence[-1] + sequence[-2]
            sequence.append(next)
    return sequence[n]
```

Nesta solução, nós iteramos até N, obtendo os números, desde o primeiro até N-1, N-2 e eventualmente o N que queremos.
Porém, existem outras formas de resolver o mesmo problema! Veja por exemplo:


```
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```
Notou como dentro da implementação desta solução, a função chama ela mesma? Que raios é isso?! Calma, já vamos chegar lá.

#recursividade
Uma função que chama a si mesma é chamada de recursiva, O processo para executar , tal função recursiva, é chamada de recursividade.
A recursividade é um dos métodos para a resolução de grandes problemas. Dito isso, um problema submetido, a uma solução recursiva, será quebrado em subproblemas menores até chegar a uma parte tão pequena que o torna possível solucioná-lo trivialmente. Um exemplo visual que podemos relacionar a essa tática de resolução de problema, são as bonecas russas, que dentro de si tem diversas outras bonecas, cada vez menores.
Vamos a outro exemplo

# Whiteboard Interview: ReverseCorp

Suponha agora que voce esta fazendo o processo seletivo para a ReverseCorp, uma empresa que se especializa em produtos e serviços ao contrario. Na  sua entevista, o seu desafio é demonstar as suas abilidades de inversão com o seguinte problema.

"Faça uma function que receba uma lista e retorne na ordem reversa

# Iterativo vs. Recursivo
Eis uma solução que vamos usar de exemplo. A este método, que já conhecemos, chamamos de método Iterativo.

```
def reverse(list):
    reversed_list = []
    for item in list:
        reversed_list.insert(0, item)
    return reversed_list
```

Porem, lembre -se onde podemos aplicar a interação, podemos tambem aplicar recursão. E as vezes, a solução recursiva fica ate mais simples! **Quando dominamos a recursão, ha nuitos problemas que podemos resolver rapidamente algo que, de outra forma, seria, muito trabalhoso de iplantar.**
Uma solução recursiva;

```
def reverse(list):
    if len(list) < 2:
        return list
    else:
        return reverse(list[1:]) + [list[0]]
```

Aqui, sabemos que se a lista tiver somente um elemento, ela invertida é ela mesma; E, caso seja uma lista maior, basta colocar o primeiro elemento por último, e depois inverter o resto! É uma forma bem interessante de ver o problema, não acha?
Note dois fatos importantes, que as soluções recursivas de ambas as entrevistas whiteboard que fizemos hoje tiveram em comum:

- começando tratando o caso mais simples de maneira trival.
- Depois, generalizam o resto dos casos , guiando-os na direção do caso trival.


# Leis da recursão
Todos os algoritmos recursivos devem obedecer a três leis importantes:

1. **Um algoritmo recursivo deve ter um caso base**  quando falamos de recursão, devemos sempre lembrar do caso base, pois sem ele nosso algoritmo ficará executando infinitamente. O caso base é a condição de parada do algoritmo recursivo, ele é o menor subproblema do problema, tornando-o possível de resolvê-lo de forma direta/trivial;
2. **Um algoritmo recursivo deve mudar o seu estado e se aproximar do caso base** : após o início da execução de um algoritmo recursivo, a cada nova chamada a ele mesmo, o seu estado deve se aproximar cada vez mais do caso base. Por exemplo, vamos imaginar o seguinte: queremos criar um código que irá printar números a partir de 0 e terminar em 10. O caso base do algoritmo é 10 , pois é onde nossa função recursiva deve parar a execução. A primeira chamada a função terá o número 0 passado de parâmetro. A cada nova chamada à função, nosso estado deve incrementar o valor 1 ao valor do estado anterior, até chegar ao número 10. Logo, o valor do estado na primeira chamada será 0, na segunda chamada será 1, na terceira chamada será 2, e assim por diante até chegar ao valor do caso base;
3. **Um algoritmo recursivo deve chamar a si mesmo, recursivamente** : Essa lei é a própria definição de recursão.

# Entendendo recursividade e colocando em prática
Antes de vermos como acontece a "mágica" da recursividade, vamos ver como costuma ser uma estrutura básica de uma função recursiva:

Nome da função e parâmetro:
    Condição de parada

    Chamada de si mesma

Declaramos uma função com um parâmetro. Dentro da função criada, definimos qual é a condição de parada da função. A condição de parada faz uma comparação entre o valor da condição com o parâmetro que a função está recebendo. Caso a condição não se satisfaça, a função é chamada novamente com um novo parâmetro. Caso contrário a execução para na condição de parada.


```
def countdown(n):  # nome da função e parâmetro
    if n == 0:  # condição de parada
        print('FIM!')
    else:
        print(n)
        countdown(n - 1)  # chamada de si mesma com um novo valor


countdown(5)
```
No código acima temos uma função recursiva que chamamos de countdown . A ideia da função é fazer uma contagem regressiva de 5 até 0. Dito isso, primeira chamada que fazemos à função passamos o parâmetro inicial, no caso o número 5 . Nas outras vezes que a função for chamada é que vamos suprir a segunda lei da recursão , passando n - 1 , sendo n o número passado por parâmetro.
Exemplo da execução do código:

```
n = 5 -> não satisfaz a condição de parada / chama a função novamente: `countdown(5 - 1)`.  # primeira execução

n = 4 -> não satisfaz a condição de parada / chama a função novamente: `countdown(4 - 1)`.  # segunda execução

n = 3 -> não satisfaz a condição de parada / chama a função novamente: `countdown(3 - 1)`.  # terceira execução

n = 2 -> não satisfaz a condição de parada / chama a função novamente: `countdown(2 - 1)`.  # quarta execução

n = 1 -> não satisfaz a condição de parada / chama a função novamente: `countdown(1 - 1)`.  # quinta execução

n = 0 -> satisfaz condição de parada / entra no if e printa "FIM!".                         # sexta execução
```
Agora que entendemos melhor o código de uma função recursiva, vamos entender o que está acontecendo "por baixo dos panos". Para isso, precisamos, primeiro, entender alguns conceitos sobre pilha de execução:

- Toda vez que chamamos uama função em um programa , o sistema operacional reserva memoria para as variaveis e parametros da função
- sempre que uma função é executada ela é guardada na pilha
- quando a função termina de serr executada, ela sai da pilha.

  Nota: Não se preocupe em entender, nesse momento, 100% dos conceitos de pilha, você irá ver esse conceito mais para frente. O importante aqui é que você entenda a parte conceitual do funcionamento da recursividade!


Podemos perceber que cada vez que a função countdown é chamada, um novo dado é adicionado à uma pilha (canto direito do gif). É adicionado à pilha todos os valores executados, do 5 ao 1, até chegarmos no caso base 0 . Quando a execução acaba, os dados são retirados da pilha, um a um, de forma reversa (do 0 ao 5), até que a pilha esvazie e o processamento finalize.

Vamos ver outro exemplo para fixarmos mais esse conceito. Dessa vez, vamos fazer um algoritmo recursivo para cálculo de fatorial. Vamos para o código!

```
def factorial_recursive(n):  # nome da função e parâmetro
    if n == 1:  # condição de parada
        return 1

    else:
        return n * factorial_recursive(n - 1)  # chamada de si mesma com um novo valor


factorial_recursive(5)
```
Nessa função acontece, "por baixo dos panos", a mesma coisa que a função do exemplo anterior. Porém, explicando com outras palavras, internamente cada chamada recursiva à função adiciona um frame de pilha, até chegarmos ao caso base. Então, a pilha começa a se desenrolar à medida que cada chamada retorna seus resultados:


# Novamente, Interativo x Recursivo

Agora, vamos ver que é possivel ter funções tanto recursivas, quanto interativas para o mesmo problema. Para isso, vamos utilizar os exemplos que usamos.
Vamos começar olhando para a função recursiva de contagem regressiva, Conseguimos montar uma função interativa para ela? sim
Olha como fazer

```
def iterative_countdown(n):
   while n > 0:
       print(n)
       n = n - 1
   print("FIM!")

   return n


iterative_countdown(5)
```
Vamos ver agora como fica o código iterativo de cálculo de fatorial:

```
def iterative_factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


iterative_factorial(5)
```
Como vimos anteriormente escolher entre uma solução recursiva ou iterativa, depende muito do que estamos buscando. Escolher uma solução recursiva não significa ganho de performance, muito pelo contrário, grande parte das vezes, a solução iterativa será mais performática. Escolher a solução recursiva terá um ganho na diminuição de complexidade do código do seu projeto. Aqui, complexidade significa legibilidade. Ou seja, nosso código fica mais simples, mais elegante, quando utilizamos recursividade.

# Análise de algoritmos recursivos
para conseguirmos realizar a analise de algoritimos recursivos, nós  iremos fazer uso da **Arvore de Recorrencia!** o que é isso ?

# Arvore de Recursão
O metodo da arvore de recursão pode ser utilizado para estimar o custo de um algoritimo. È um meio de analisarmosseu custo. o que nos ajuda a decidir se tal solução recursiva vale a pena ou não. Podemos visualizar nivel a nivel da estrutura  de um algoritimo recursivo por meio de uma arvore recursiva. No final, tem-se a estimativa de tempo do problema. Vamos ver:

```
def fibonacci(num):  # nome da função e parâmetro
    if (num <= 1):  # condição de parada
        return num
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)  # chamada de si mesma com um novo valor
```
Acima estamos fazendo um código recursivo para cálculo de fibonacci. Na imagem abaixo visualizamos a representação do algoritmo fibonacci recursivo, que acabamos de montar, convertido em uma estrutura que chamamos de árvore:

Cada nó da árvore acima representa o custo da solução de um subproblema. Quando olhamos para a árvore como um todo, ou seja, quando expandimos ela, podemos somar todos os custos de cada nível da árvore e depois teríamos o resultado total do problema. O problema começa com apenas um nó e vai decompondo até alcançar os casos base, que são as "folhas" da árvore. Folhas são, basicamente, nós da estrutura que não possuem nenhum nó abaixo deles.

Exemplo retirado do site: www.visualgo.net/en/recursion
💡 Lembre-se! Se você se embananar com as estratégias de análise de recursão, fique tranquilo(a), é um assunto mais desafiador e com o tempo e experiência esse conhecimento vem. E não deixe de falar com a gente no Slack se algum exemplo estiver te confundindo!
Ou seja: desenhe todas as recursões do problema até chegar aos casos base e some as complexidades! Fique de olho nas proporções! Se cada subproblema é O(n) e você criou um para cada elemento da sua entrada de tamanho n , você tem aí uma complexidade O(n * n) , ou seja, uma complexidade quadrática. Se, por outro lado, a cada subproblema você dividiu o tamanho do problema original por dois, você gerará log n subproblemas. Se cada um desses custa O(n) , você teria uma complexidade O(n* log n)
A forma de traduzir a lógica da árvore de recursão para uma notação puramente matemática se chama Teorema Mestre ! N

### Principais cuidados ao usar recursão
Como visto, chamadas de funções ocupam memória já que, toda vez que uma chamada é feita, o SO reserva memória para as variáveis e parâmetros. Quando um loop recursivo é muito grande, ele fará muitas chamadas, e quando ele faz muitas chamadas podemos ter um stack overflow (que não é apenas o fórum de ajuda para devs 😂). O stack overflow, ou estouro de pilha em português, significa que ficaríamos sem memória para continuar com a execução do programa.
Para evitar um estouro de pilha, é importante que as chamadas recursivas parem. Para que consigamos fazer as chamadas recursivas pararem é importante lembrarmos sempre de implementar a condição de parada na função .

Apesar de funções recursivas serem mais elegantes e mais fáceis de implementar, elas costumam ser menos eficientes que do que as iterativas, por causa do overhead de empilhar e desempilhar chamadas de funções.
Não é tão simples decidir quando usar uma solução recursiva para um problema, mas você vai perceber que alguns problemas são muito mais fáceis e intuitivos de serem resolvidos recursivamente. É nesses casos que a recursão vale a pena.

# Estratégias para solução de problemas
Durante todo o conteúdo falamos e vimos muito sobre "algoritmo", nessa sessão não será diferente! Vamos ver diferentes lógicas que podemos aplicar à um algoritmo para a resolução de um problema.
Nos deparamos com diversos problemas diferentes no nosso dia a dia e na nossa vida. Na nossa carreira como pessoa desenvolvedora não será diferente!

Como diria Brad Miller e David Ranum no livro Resolução de Problemas com Algoritmos e Estruturas de Dados usando Python , escrito por ambos, e traduzido pela USP, "a ciência da computação é muitas vezes difícil de definir. Isto é provavelmente devido ao infeliz uso da palavra 'computador' no nome. (...) A ciência da computação é o estudo de problemas, resolução de problemas e soluções que surgem do processo de resolução de problemas. "

# Iterativa

A solução iterativa é caracterizada pela repetição de uma determinada operação, procurando resolver algum problema encontrando sucessivas aproximações, a partir de uma suposição inicial. A ideia nesse tipo de processo é repetir um determinado cálculo várias vezes, obtendo-se a cada repetição, ou iteração, um resultado mais preciso que aquele obtido na iteração anterior. A cada iteração, utiliza-se o resultado da anterior como parâmetro de entrada para o cálculo seguinte. O resultado é uma sequência de valores aproximados, não exatos, mas que estão dentro de uma faixa de erro aceitável.

# Força bruta

A força bruta, também conhecida como tentativa e erro ou busca exaustiva , é a estratégia mais trivial e intuitiva para solução de problemas. Ela consiste basicamente em enumerar todas as combinações possíveis para uma solução e avaliar se satisfazem o problema. Dessa forma, é possível escolher a melhor das soluções, ou seja, a solução ótima, mas apesar de trivial, em alguns casos, a força bruta possui desempenho geralmente muito ruim.

Vamos solucionar um problema chamado de problema da mochila , com a força bruta:
Dada uma mochila com capacidade C , e n objetos com peso (i = 1...n), deve ser possível preencher a mochila com o maior peso total, respeitando a capacidade C .
Suponha uma mochila com capacidade de 15kg e objetos de peso 12kg, 2kg, 4kg e 8kg.
Este problema possui mais que uma solução ótima, ou seja, possui soluções ótimas equivalentes:

```
Uma solução ótima: 12kg + 2kg = 14kg;

Outra solução ótima: 8kg + 2kg + 4kg = 14kg.
```
Soluções viáveis seriam, entre outras:

```
- 12kg;

- 2kg;

- 4kg;

- 8kg;

- 2kg + 4kg.

# ........
```
No caso acima, as soluções são viáveis, porém não são ótimas. Elas não são ótimas, pois a mochila está sendo preenchida, mas não está sendo preenchida chegando mais próximo possível ao peso máximo. Por exemplo, uma das soluções que temos acima é preencher a mochila com um objeto de 2kg apenas, sendo que a mochila suporta 15kg.
Um exemplo de uma solução inviável seria, entre outras:

```
- 12 kg + 4 kg = 16kg.
```

O caso acima é inviável, pois o peso máximo que a mochila comporta é 15kg. Com isso, podemos concluir que o exemplo acima é inviável, pois ultrapassa os 15kg.

Um método baseado em tentativa e erro testaria todas as combinações entre elementos checando:

- Se a solução é viável;
- Se a solução possui valor melhor que outra encontrada anteriormente.
-
Para conseguir definir qual seria a melhor solução, todas devem ser enumeradas e registradas, e, ao final, os caminhos que não chegaram a um solução final, devem ser retirados.


# Dividir e conquistar

A estratégia dividir e conquistar , também chamada de divisão e conquista, consiste em dividir o problema em partes menores, encontrar soluções para as partes, e então combinar as soluções obtidas em uma solução global.
Usar essa estratégia para resolver problemas, nos quais os subproblemas são versões menores do problema original, geralmente leva à soluções eficientes e elegantes, especialmente quando é utilizado recursividade.
A estratégia emprega modularização de programas e frequentemente conduz a um algoritmo simples e eficiente. Esta técnica é bastante utilizada em desenvolvimento de algoritmos paralelos, onde os subproblemas são tipicamente independentes um dos outros, podendo assim serem resolvidos separadamente.

  💡 A modularização de um programa consiste em dividi-lo em partes funcionais que conversam entre si, tornando o software mais eficiente.

A técnica de Divisão e Conquista consistem em três passos:

- Divisão : dividir a instância do problema original em duas ou mais instâncias menores, considerando-as como subproblemas;
- Conquista : resolver cada subproblema recursivamente;
- Combinação : combinar as soluções encontradas em cada subproblema, compondo uma solução para o problema original.

Um exemplo para ilustrar o uso dessa técnica é o algoritmo de ordenação de um vetor por intercalação, ou, como é chamado, MergeSort . Sua representação pode ser feita através de uma árvore binária, conforme a imagem abaixo:
Observe na imagem acima que o primeiro ( a ) faz a divisão dos elementos, e o segundo ( b ) de baixo para cima, faz a conquista, ou seja, resolve cada parte do problema e depois combina todas as soluções encontradas.

