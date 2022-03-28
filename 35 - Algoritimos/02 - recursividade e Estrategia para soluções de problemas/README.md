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