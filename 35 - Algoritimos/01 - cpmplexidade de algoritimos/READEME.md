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