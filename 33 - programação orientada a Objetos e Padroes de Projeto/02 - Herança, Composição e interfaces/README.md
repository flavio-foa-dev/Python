# Herança, Composição e Interfaces
### O que vamos aprender ?

Vimos, na última aula, como o **paradigma de programação orientada a objeto (POO)**, funciona  com base no conceito de objeto, entidades que podemos criar, e as mensagens que elas podem trica entre si (em outras  palavras: o comportamento que elas tem ). Hoje va,os colocar em nossa caixa de ferramentas mais recursos importantes de POO, que nos permitirão criar códigos mais organizados, com menos chance de erros e mais faceis de manter, usar e reusar no futuro!

Vamos, em suma, falar muito sobre como **compartilhar logica entre classes, criar versoes especializadas de classes e como **garantir consistencia entre classes especializadas**

### Seremos capazzes de:

- Descrever, como pilar da `programação orientada a objeto` a `Herança` a capacidade de herda, para especializar os atributos e metodos de uma classe
- Definir `Classes Abstrata`
- Definir `metodos Abstratos`, ou `funções abstrata`
- Definir, em `Programação Orientada a Objetos` , a `interface` de um classe
- Definir como boas pratica utilizar `Herança` apenas para especializar classes
- Definir como boas pratica utilizar `composição` para compartilhar um mesmo codigo entre diferentes classes
- Implementar `Metodos de classes` para `Classes` em python

### Isso é importante para
Compartilhar logica é ensencial para, reduzindo duplicação de código, nos possamos realmente ver a Programação Orientada a Objetos brilhar. Alem disso, especializar comportamento de forma consistente tambem garante, sem muito esforço, uma aplicação consistente e fácil de entender. Com acesso a ferramentas que te permitem fazer isso, o poder da Programação Orientada a Objetos se tornara enorme em suas maos

### Conteúdos
Antes de mais nada, uma observação; ao logo do dia de hoje, trabalharemos o sdesenvolvimento de um exemploe , ao final, teremos em mãoes um versão show de bola 👌 dele! Ao longo do caminho, vamos ir tentando deixar ele legal e vamos aprender sobre o que se deve e o que não se deve fazzer!

sumponha que você precise criar um software que gera **Relatorios de vendas**. Nosso programa tem que conter toda uma lógica para ler dados e criar o relatorio e, ao final, vamos gerar um arquivo imprimivel com tais dados. Um  JSON, por exemplo. Como estamos trabalhando com Orientação  a Objetos, vamos pensar! **Que entidade eu preciso criar para resolver meu problema ?**

Essa é uma pergunta que, muitas vezes, só conseguimos responder com firmeza depois de experimentar um pouco. Já que estamos fazendo um relatorio, vamos começar fazendo dele a nossa entidade! Vamos, então, criar uma entidade `SalesReport` e tentar incumbir a ela a responsabilidade de gerar o nosso relatório.

import json


class SalesReport():
    def __init__(self, export_file):
        self.export_file = export_file + '.json'

    def build(self):
        """ Aqui colocamos a lógica para a entidade 'se criar',
        ou seja, criar um relatório imprimível. Por simplicidade,
        vamos omitir essa lógica nos exemplos! """
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    def serialize(self):
        # Vamos gerar, aqui, o nosso relatório em formato JSON
        with open(self.export_file, 'w') as file:
            json.dump(self.build(), file)

PAUSA!
O que fizemos até aqui? Nós acabamos de criar um objeto e dar a ele a capacidade de responder a mensagens!

# Classe, crie (em outras palavras, instancie!) uma nova entidade 'Relatório de vendas' para eu usar!

meu_relatorio_de_vendas = SalesReport('meu_relatorio')

# Entidade 'meu_relatorio_de_vendas', que eu acabei de criar, imprima-se!

meu_relatorio_de_vendas.serialize()

Estamos, portanto, seguindo direitinho a Orientação a Objeto, certo? Colocamos nosso código em produção, ele funciona, várias pessoas o instanciam, o chamam e enviam mensagens a ele em toda nossa aplicação, pedindo para que se imprima! Agora... algum tempo passou! Te pedem para, além de gerar relatórios JSON, gerar relatórios em CSV também! Querem acrescentar algo à sua aplicação, ou seja, estendê-la! Vamos trabalhar um pouco nisso?!

### Exercício de Fixação
1. Altere o código da classe SalesReport para que ela, além de gerar relatórios em JSON, gere relatórios em CSV também. Defina, primeiro, como você fará a extensão da lógica para depois gerar o CSV mesmo. Não gaste mais que cinco minutos nesse exercício! Quando o relógio apitar, volte para a leitura que vamos refletir sobre a experiência!


### Como entender o meu codigo ?
Feito o exercicio, imagina que sua liderança técnica vai fazer um code review do seu código e te faz algumas  perguntas:

1. Para adicionar a funcionalidade você precisou mudar a **assinatura** (nome e parâmetros) **de alguma função** Se sim, você vai precisar mudar todo o codigo que usa esssa função, então não podemos fazer isso sem gerar muito retrabalho" Não podemos fazer a mudança assim.
2. os nomes das suas funções ainda estão corretas? Por exemplo, se uma se chama `Serealize_csv`, e aoutra deve se chamar `serealize_json`. chama-la so de `serialize` é confuso - se temos nais de uma serialize é qual delas?
3. Você criou uma **nova classe** Se sim, ela duplicou alguma logica? se duplicou, por exemplo, a logica de construção do relatorio, na função `build`, não rola ❌!
4. Voĉe mudou o nome da classe?  se sim, voltaremos ao problema de modificar código ja existente. Não da!

Se voce fez **qualquer uma das coisas acima**,  a sua solução trára problemas! Ou você precisara alterar várias partes do codigo para adicion ar sua funcionalidade - o que da muito trabalhoe aumenta a chance de se ter bugs - ou você duplicou logica e deixou seus nomes confusos.

Não parece ter como sair dessa enrascada, não é ? Seu codigo foi bom para demanda inicial, mas, agora, te gerou problemas. Você precisa, necessariamente, refatora-lo para introduzir uma nova funcionalidade. A missão, então, é outra: **você vai refatorar o código que escreveu** para que, no final, qualquer extensões possam ser feitas sem modificar o codogo ja existente" Um tebalho de cração de nova funcionalidade que, no futuro, poderia durar varias horas, virará um trabalho de minutos!

Como fazer então isso ? Como eu escrevo um código **Aberto para extenções, mas fechado para modificações ?**

Para o nosso caso, a chave da questão é usar um dos **grandes pilares da Programação Orientada a Objetos!** Falamos de abstração, encapsulamento... e agora vamos falar de **Herança**


