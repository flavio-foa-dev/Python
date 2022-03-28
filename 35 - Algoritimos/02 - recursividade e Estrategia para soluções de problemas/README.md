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
Assim por diante: 8, 13, 21, 33, 54 ...
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