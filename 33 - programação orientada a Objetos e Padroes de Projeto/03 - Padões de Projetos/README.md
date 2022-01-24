# Padrões de Projeto
### O que vamos Aprender ?

Hoje é o dia de boas praticas! criar objetos de maneira eficaz  requer pratica e, no começo. você vai refatorar muito código a cada vez que uma demanda chegar, ao perceber que sua forma de separar seu código em entidades não foi a melhor possivel para evitar duplicidade de código e facilitar o entendimento.

Vamos ensinar algumas coisas pra você  ter na sua caixa de ferramentas para. no tempo, te ajudar a construir objetos bons de cara, sem precisar refatorar tanto. Você vai aprender o que são padrões de projeto: formas classicas de resolver problemas que costumam aparecer muito! Alem disso, apresentaremos os principios  SOLID. que ainda não vimos em Back-End. por fim, você vera coo reconhecer indicios de problemas, os code smells, e se aproveitar dessa oportunidade para realizar refatorações de codigos.

Guarde o conteúdo de hoje nos seus favoritos, porque você achará interessante consultá-lo várias vezes no futuro, especialmente quando estiver trabalhando em aplicações grandes! Hoje aprenderemos conceitos e veremos vários exemplos. Na medida em que você for ganhando vivência e experiência no mercado, mais e mais o aprendizado de hoje se consolidará!

### sera capaz de :
- Definir um Padrão de Projeto de
- Enumerar code smells e trata-los
- Aplicar todos os principios S.O.L.I.D.

## Isso é importante para:

em uma rotina de desenvolvimento de software, escrever um codigo que resolva o problema é a parte facil do trabalho. A pare dificil, e a mais comum, é quando você tem que ler um código que esta escrito, ou seja, fazer a manutenção de codigo.

Todo software, desde seu desenvolvimento ate o fim de sua vida util, precisa de manutenção. Atualizações de funcionalidades, adaptação a mudanças em plataformas ou bibliotecas, descobertas de bugs ou falhas de seguranças.

Para assegurar que software é facil de entender e ser alterado, seja por quem o escreveu ou seja por novas pessoas entrando no time de desenvolvimento, ultilizando padões; regras que nos ajudem a desviar de erros comuns, e saber o que esperar ao encontar um codigo novo em que precisamos trabalhar, Imagine uma enciclopedia, por exemplo. Sabemos que por paãoes por padrão, todos os artigos estão em ordem alfabética; portanto, é fácil encontrar o que precisamos. O mesmo vale para um código que sabemos que obedece a um padrão de projeto.

Porém, ninguém é perfeito; neste contexto de constante desenvolvimento e manutenção, podem surgir certos problemas que não necessariamente impactam a funcionalidade do software, mas afetam a legibilidade e manutenibilidade do código.
Identificar a presença destes problemas e recomendar uma solução é um dos papéis de uma pessoa desenvolvedora.

# Liskov Substitution Principle

Lembra dos princípios S.O.L.I.D.? Este é o L, o Princípio de Substituição de Liskov . Vamos botar a mão na massa com um exemplo bem robusto; são nestes exemplos que a organização vale mais a pena! Bora?
Suponha que o seu time de desenvolvimento está trabalhando em um software que controla os acessos à API do seu serviço. Você está responsável por manter um código cujo dever é gerar uma token de acesso, que o front utilizará para validar todas as requisições que receber de clientes.
Sua empresa cobra clientes por número de requisições, então você precisará registrar em um banco a quantidade de vezes que uma determinada token foi utilizada para acessar o serviço. Porém, o seu time considerou os seguintes fatos:
Nossa infra-estrutura utiliza um servidor SQL, cuja inserção tende a ser mais lenta.
É normal que clientes acessem o serviço milhares de vezes em um intervalo de 30 minutos, e depois fiquem vários dias sem utilizar.
Então vocês decidiram guardar as contagens de requisições em um banco de dados cache , que fica armazenado por inteiro na memória RAM de uma máquina! Por estar nessa memória, ele é super rápido mas não pode ser muito grande. Decide-se que o valor é armazenado no banco em cache e, após o valor ficar uma hora inteira sem ser atualizado, ele é enviado para o banco SQL.
Sua colega Bia hoje trabalha no serviço, e utiliza a seguinte classe para acessar o banco de dados SQL:

import pysql  # Encare essa lib como fictícia!

class SqlConnector:
    # ...

    def __init__(self, address, port):
        print(f'criada uma conexão em {address}:{port}')
        self.db = pysql.connect(address, port)

    def get_count(token):
        query = f'SELECT count FROM access WHERE token={token};--'

    def count_request(token):
        query = f'UPDATE access SET count = count+=1 WHERE token={token};--'
        self.db.execute(query)

Nosso dever é implementar o acesso ao Redis, nosso banco de dados cache , e oferecer à Bia uma interface amigável e fácil de utilizar. Ou seja, funções que ela possa chamar em seu código de forma simples.
(Redis é um banco de dados em memória, que utiliza uma estrutura chave-valor. Saiba mais indo nos recursos adicionais!)
Assim, criamos a seguinte classe, implementando a lógica de cache:


import pyredis  # Encare essa lib como fictícia também!

class RedisConnector:
    def __init__(self, address, port):
        print(f'criada uma conexão em {address}:{port}')
        self.db = pyredis.connect(address, port)

    def get_count(token):
        result = self.search(token)
        amount = result.get("access_count", None)
        return amount

    def update_count(token):
        amount = self.get_count()
        if amount is None:
            self.db.insert({token:1})
        else:
            self.db.insert({token: amount+1})

Porém, ao analizar este código a nossa colega Bia não gostou! Ela disse:
Mas aí vamos ter que refatorar muita coisa! Eu uso o conector SQL em muitos lugares, e preciso ser capaz de usar o conector Redis em todos eles! Se o nome das funções mudarem eu vou ter que refatorar o código inteiro! E se pudéssemos chamar os dois conectores da mesma forma, nos mesmos lugares? Isso facilitaria demais.
Com este feedback, refatoramos as classes conectoras. Vamos criar uma classe Connector, que abstrai os métodos que devemos utilizar numa interface , e os dois conectores serão herdeiros desta classe. Veja:

from abc import ABC, abstractmethod

class Connector(ABC):
    @abstractmethod
    def get_count(token):
        pass

    @abstractmethod
    def count_request():
        pass

class RedisConnector(Connector):
    def __init__(self, address, port):
        # A lógica da conexão ao banco Redis

    def get_count(token):
        # A lógica de acesso ao banco Redis

    def count_request(token):
        # A lógica de acesso ao banco Redis

class SqlConnector(Connector):
    def __init__(self, address, port):
        # A lógica da conexão ao banco SQL

    def get_count(token):
        # A lógica de acesso ao banco SQL

    def count_request(token):
        # A lógica de acesso ao banco SQL


Agora, uma classe que precisar acessar o banco pode receber como Connector tanto uma classe quanto a outra! Veja um exemplo de uso:

import analyzer

# o parâmetro database é um connector
def analyze_data(token, database, data):
    try:
        report = analyzer.complete_report(data)
        database.count_request(token)  # Cliente receberá cobrança
        return report

    # Se a database não tiver o método count_request, vai lançar o erro
    # AttributeError -- e a gente deixa o programa travar se isso acontecer.
    except analyzer.InvalidDataException:
        # A gente lida apenas com InvalidDataException, que é um erro
        # esperado quando o relatório não estiver pronto.
        return  # Cliente não receberá cobrança, pois não geramos o relatório


Note que, dentro deste código, não conseguimos distinguir qual conector estamos usando. Tudo o que nos interessa aqui é que ela tem um método count_request() que recebe a token de acesso. Assim, se estivermos trabalhando nesta parte da aplicação, podemos ter certeza de a inserção em banco foi feita, sem nos preocuparmos com a lógica de cache que está acontecendo por trás. Nossa colega Bia conseguirá trabalhar de forma muito mais eficiente.
🎉 Acabamos de utilizar o L da arquitetura SOLID!
L iskov substitution principle ( Princípio de substituição de Liskov ): objetos em um programa devem ser substituíveis por outros de suas classes herdeiras, sem que isso quebre nada. Isso significa que, para a substituição ser possível, os subtipos devem seguir a interface de um tipo base;
Ou seja, classes herdeiras devem sempre respeitar a interface de suas classes ascendentes! Elas podem especializar comportamentos, mas nunca removê-los! Caso contrário seu código fica cada vez mais difícil de usar, reusar e entender o que se faz! Agora, a Bia continuará fazendo suas chamadas da mesma forma, sem refatorar seu código. Esta é a parte legal da orientação a objetos bem feita!
E não precisamos, lembrem, escrever um código ruim e depois refatorar (embora, fatalmente, isso vá acontecer às vezes, hehe); se lembrarmos dos princípios S.O.L.I.D. enquanto estivermos decidindo como as classes devem ser, já pulamos muitos desses passos de refatoração e já teremos, de cara, um código muito melhor.
Porém, nenhum código é perfeito. A abstração e as boas práticas servem para ajudar, mas repito: Não existe bala de prata . O bom senso e a experiência são muito importantes também. No fim, o objetivo é ter um código simples.

# Interface Segregation Principle

O Vini, seu colega, estava recentemente resolvendo o problema do banco de dados SQL estar recebendo acessos demais, causando sobrecarga e crashes. Após explicar este problema, ele explicou a solução:
Fiz uma réplica do nosso banco de dados. A maioria dos acessos era de leitura, então com esta réplica read-only, poderemos dividir os acessos entre cada um dos dois, evitando a sobrecarga. Aí quando for um acesso de escrita, podemos contar com o meu replicador pra manter os dois bancos iguais.
Massa. Pra atender essa demanda, o Vini pediu que os trechos do sistema que só precisam ler dados utilizassem conectores que só conseguem ler, evitando confusões. Combinados precisam ser codados, não é?
Só que nós temos uma interface de conector que implementa operações de leitura e escrita. E agora precisamos de uma interface somente com leitura, sem escrita! Como conseguimos fazer isso?
Primeiro, devemos considerar a abstração em que trabalhamos ao atender as demandas anteriores. Devemos manter uma boa abstração, para que o nosso codigo continue simples e fácil de manter. Então, nosso objetivo principal é assegurar duas coisas:
As classes ReadOnlyConnectors devem implementar apenas o método get_count .
Já as classes que forem FullConnectors devem implementar, pelo menos, get_count e count_request .
Lembrando dos conceitos de Classes Abstratas, já sabemos como fazer isso! Classes Abstratas e Herança são formas que temos de garantir que as classes herdeiras precisam ter certos comportamentos. Vamos tentar abstrair estes comportamentos.

''' ABC é uma Abstract Base Class. Herdar desta classe indica que estamos fazendo
uma classe abstrata, que neste caso também é uma Interface, pois não contem
implementações, apenas definições de métodos.

Estes metodos DEVEM ser implementados pelas classes herdeiras, por isso
utilizamos o decorator `@abstractmethod`: se estes metodos não forem sobrescritas por
uma implementação da classe herdeira, o Python nos avisará que estamos cometendo um erro.'''

from abc import ABC, abstractmethod

class ReadOnlyConnector(ABC):
    @abstractmethod
    def get_count(self, token):
        pass

# Como FullConnector deve também ser capaz de ler,
# ela é uma classe abstrata que herda de outra classe abstrata!
class FullConnector(ReadOnlyConnector):
    @abstractmethod
    def count_request(self, token):
        pass

## Uma classe abstrata exige a implementação de todos os seus métodos.
## Uma implementação incompleta não poderá ser instanciada!
## class SQLConnector(FullConnector):
##     def count_request(self, token):
##         ...
##
## TypeError: não pode instanciar porque não implementa o método get_count
## sql = SQLConnector()

Com estas interfaces, podemos escolher quais características estarão presentes em cada conector que criarmos. Por exemplo:

class ReadOnlySqlConnector(ReadOnlyConnector):
    # ...
Este conector SQL terá somente os métodos de leitura, sendo ideal para utilizar com a réplica que o Vini criou.

class RedisConnector(FullConnector):
    # ...

Já este conector pode ser usado pela Bia, que precisa anotar os novos acessos!
Esta divisão de tarefas onde cada interface tem a responsabilidade de representar uma única característica é chamada de Princípio De Segregação de Interfaces , ou em inglês, Interface Segregation Principle. Justamente o I dos nossos princípios S.O.L.I.D.!
Interfaces, como toda abstração, são "contratos" feitos em código para nós pessoas desenvolvedoras, para que possamos nos organizar melhor. As interfaces garantem que tudo estará organizado, e respeitando estes contratos. Não faça interfaces grandes, faça interfaces pequenas com responsabilidades únicas@
"Nosso contrato não vale nada se não estiver codado,"
Vini, citando Clarice Lispector, 2021

Exercícios de fixação

Agora que conhecemos todos os 5 princípios S.O.L.I.D., relembre cada um deles, e reflita como todos eles se complementam para nos ajudar a escrever um código que, desde o início já precisará de menos refatorações conforme o sistema cresce e muda ao longo do tempo. Lembre-se deles:
S - Single Responsability Principle - Princípio da Responsabilidade Única
O - Open/Closed - Aberto para extensão, fechado para modificação
L - Liskov's Substitution Principle - Principio da Substituição de Liskov
I - Interface Segregation Principle - Principio da Segregação de Interfaces
D - Dependency Inversion - Inversão de Dependências (ou: use composições!)

## O que é padrões de Projeto
Padrão de Projeto é uma solução geral para um problema que ocorre com frequência dentro de um determinado contexto no projeto de software . Desde a década de 70, cientistas da computação perceberam que, ainda que em contextos diferentes, algumas soluções de problemas se repetiam em vários softwares . Visando facilitar a reutilização do desenho da solução e a comunicação, assim como melhorar a documentação e compreensão de um sistema, essa comunidade de cientistas começou a catalogar estes padrões.
Para deixar tudo mais tangível, responda à seguinte pergunta: "Quantas aplicações no mundo precisam iterar sobre uma lista de elementos?" Certamente milhares, senão milhões, correto? Eventualmente se propôs uma forma padronizada de implementar a solução para este problema, e tal proposta foi adotada, e este é o padrão de projeto conhecido como iterator . Ao receber uma lista de entidades , uma classe que implementa o padrão de projeto iterator deve ter uma interface específica: por exemplo, uma função next que retorna o próximo elemento da dita lista.
Não interessa se a sua lista é em formato de array , de árvore, se é uma lista de inteiros, objetos ou o que for. Ao garantir que sua classe possui um iterador , você garante que ela tem uma função next que vai acessar o próximo elemento da sua lista. A forma de fazer isso é você quem define. Ao seguir o padrão de projeto, você organiza o seu código - e o seu raciocínio - de uma forma pensada, estudada e comprovadamente eficaz.

O exemplo do iterator é um exemplo mais básico do que padrões de projeto são, mas ilustra bem o seu propósito: organizar seu código e raciocínio de formas eficazes, comprovadamente boas e (praticamente) universalmente aceitas. Ao se deparar com um determinado problema que se encaixa na definição de um padrão de projeto, busque o padrão de projeto para saber uma forma boa de resolver esse problema.
Um padrão é definido e documentado com um nome, o problema que busca resolver, uma solução dada por ele e as consequências sobre esta escolha. São documentados em formas de explicações e diagramas abstratos, possibilitando assim a utilização em diferentes contextos. Quando falamos de Padrões de projeto , é impossível deixar de falar sobre o livro da 'gangue dos quatro' . Hoje em dia, porém, muitos outros padrões estão documentados em diversas outras literaturas. É importante conhecer diferentes padrões e onde se aplicam, mas não fique preso a eles. Outros padrões podem emergir dos seus códigos e nem sempre estarão documentados.

## Interator

class DatabaseIterable:
    def __init__(self, sql_connector, query_template):
        self.db = sql_connector
        self.query_template = query_template

    def get_page(self, page):
        return self.db.get(query=self.query_template, page=page)

    def __iter__(self):
        """Aqui iniciamos a iteração, retornando um objeto DatabaseIterator
        como Iterador."""

        return DatabaseIterator(self.db)


class DatabaseIterator:
    def __init__(self, sql_connector):
        """No construtor da classe iteradora definimos o valor inicial do
        contador current_page, e também o(s) atributo(s) que será(ão)
        responsável(is) por armazenar/acessar a coleção de dados pela qual
        queremos iterar."""

        self.db = sql_connector
        self.current_page = 0

    def __next__(self):
        """Este método busca no banco de dados a página que queremos e
        incrementa o contador current_page, para retornarmos a próxima página
        na próxima vez que o método for chamado."""

        data = self.iterable.get_page(page=self.current_page)

        """É uma boa prática a utilização da exceção StopIteration() para
        indicar que não foi possível avançar na iteração. Ou seja: tentamos
        acessar uma current_page que não existe."""

        if not data:
            raise StopIteration()

        self.current_page += 1
        return data

Note que cada vez que chamarmos o método next() na instância retornada por iter() , receberemos uma parte pequena dos dados, que o Beto pode utilizar na sua ferramenta de relatórios.

Mas espera um pouco, esse negócio de acessar partes pequenas de um conteúdo maior, uma de cada vez, acho que já vimos isso em algum lugar, não?
Veja

minhas_linguagens = ["javascript", "python", "C", "Go"]
for linguagem in minhas_linguagens:
    print("Eu sei programar em: ", linguagem)

lista_de_compras = open("compras.txt", "r")
for item in lista_de_compras:
    print("Eu devo comprar: ", item)

O padrão iterator é aplicado para facilitar e unificar a resolução de todos os problemas que encontrarmos que são similares a "preciso operar sobre vários elementos, mas um de cada vez". É implementado de várias formas em diferentes linguagens, sempre buscando facilitar a nossa vida.
No Python por exemplo, quando chamamos um for para iterar sobre um objeto, a linguagem envia para o mesmo a mensagem __iter__() , de modo a obter um iterador ; em seguida, envia para o iterador a mensagem __next__() para encontrar o próximo item, e o próximo, e o próximo... até o iterador se esgotar (levantar a exceção StopIteration() )! Assim, toda classe que implementar o padrão Iterator pode ser usado com estruturas como o for ! Listas, tuplas, dicionários, árvores, até arquivos.
Por exemplo, nosso iterador do banco de dados poderia ser acessado assim:

# Primeiro instanciamos o ITERÁVEL
post_paginator = DatabaseIterable(db, post_page_query_template)

# Em seguida podemos usar o for pra iterar
# o ITERADOR é criado implicitamente
for page in post_paginator:
    # faz algo com a pagina, que é uma lista de resultados
    for post in page:
        print(post['title'])

Exercícios de fixação
Em seu terminal Python, crie uma nova lista, uma lista normal, com alguns elementos. Agora, chame o método __iter__() desta lista, e veja que é retornado um objeto list_iterator
Guarde este objeto em uma varável, e chame o seu método __next__() para ver o que acontece!

## Adapter

Vamos voltar ao nosso trabalho nos conectores! O Beto te trouxe uma demanda nova:
O problema agora é outro: a ferramenta que compramos tem uma API pronta pra integrar no nosso sistema! Só que a interface é muito diferente da nossa, ela exporta uma lista de cabeçalhos e uma lista de valores, não é como a nossa que já monta os dicionários direitinho...
Vai dar MUITO trabalho utilizar esta ferramenta, vamos ter que parar tudo para adaptar o nosso sistema a esse formato! Ou pior, vamos ter que REIMPLEMENTAR a api que eles oferecem >:(
Calma Beto, sem pânico! Podemos solucionar isto. O que podemos fazer?

class ReportAnalyzer:
    def __init__(self, loader):
        self.loader = loader

    def average(self):
        # este é um dos métodos que espera uma lista de dicionários
        data = self.loader.load_data()
        # aqui ela soma o valor na chave final_price em cada item da lista
        total = sum(order['final_price'] for order in data)
        return total / len(data)

    ...

O código acima é o código do nosso sistema, que espera que os loaders retornem uma lista de dicionários. Mas olhem no exemplo abaixo como a ferramenta retorna os dados:

from gerenciator3000 import ReportLoader

loader = ReportLoader()
print(loader.headers)   ##  ['id', 'date', ..., 'final_price']
print(loader.rows[0])  ##  [1337, '2020-11-20', ..., 2350.5]

Tire um minuto para pensar no que você faria para que o Beto consiga aproveitar os dados e fazer o relatório! A meta é evitar re-escrever o ReportAnalyzer , ou mesmo o gerenciator3000.ReportLoader que a gente nem sabe como funciona!
pensa, pensa, pensa
Bom, após muito chá de camomila, nosso time decidiu que faríamos uma classe responsável por "traduzir" estes dados, do formato da ferramenta para o formato do nosso sistema. Esta classe poderá ser acoplada na ferramenta de relatórios.
Veja o que fizemos:

class G3000LoaderAdapter:
    # aqui o loader é uma instancia do gerenciator3000.ReportLoader!
    def __init__(self, loader):
        self.loader = loader

    def load_data(self):

        # o zip junta uma lista de chaves e uma lista de valores
        # e cria um dicionário! por exemplo:
        # zip(['nome', 'idade'], ['Capi', 34]) => {'nome': 'Capi', 'idade': 34}

        return [zip(loader.headers, row) for row in loader.rows] # tcharans

Lindo! Acabamos de utilizar outro padrão, chamado Adapter . Ele permite converter a interface de uma classe em outra interface, esperada pelo cliente (isto é, o código que usa a nossa classe). O Adapter permite que interfaces incompatíveis trabalhem em conjunto – o que, de outra forma, seria impossível. Veja só:

from gerenciator3000 import ReportLoader
from project.loaders import G3000LoaderAdapter
from project.analyzer import ReporterAnalyzer

# o loader da ferramenta é carregado do jeito que a ferramenta recomenda
g3000_loader = ReportLoader(...)
# o adaptador recebe o loader da ferramenta.
loader = G3000LoaderAdapter(g3000_loader)
# o analyzer do nosso sistema recebe o adaptador como qualquer outro loader.
analyzer = ReportAnalyzer(loader)

analyzer.average() # JUST WORKS (tm)

Nossa aplicação aumenta em complexidade como consequência, pois estamos adicionando novas interfaces e classes, porém o desacoplamento entre o código do cliente e o objeto adaptado se mantém. Mudanças no objeto adaptado se refletem apenas no adaptador e não no código cliente, então você não altera nenhuma lógica para adicionar a funcionalidade. É possível substituir o serviço adaptado através da criação de novos adaptadores.
Classes se comunicam através de troca de mensagens, porém nem sempre isso é possível de se fazer diretamente. Às vezes há uma incompatibilidade entre as classes (tipo uma classe esperar CSV e outra só enviar JSON!), seja por causa de um código legado ou contextos distintos. Em outras palavras, as classes precisam se comunicar, mas é difícil fazê-las "conversarem".


Quando as mensagens que as classes utilizam para se comunicar estão em "linguagens distintas", não podemos simplesmente mudar a linguagem; isso iria quebrar todos os outros lugares em que esta classe é utilizada! Uma terceira entidade, que faz a "tradução" é normalmente a saída mais organizada.
Exercício de fixação
Olhe ao seu redor e tente identificar objetos que fazem o papel de um Adapter: um objeto que é necessário para que duas outras coisas funcionem juntas, que não conseguiriam funcionar juntas sem este adaptador.

## Strategy
O Beto quer mais uma coisa! Sabe esses relatórios tão grandes? Agora a empresa cliente quer entregá-los de forma compactada para clientes, em .zip . Além disso, para transito nos servidores, o time técnico quer compactar os servidores em .gz . Você, felizmente, já fez isso na aula passada 😎
Strategy é um padrão que você já viu na aula passada! Você tem uma tarefa que pode fazer de diversas formas diferentes. Por exemplo, compactar um arquivo de duas formas diferentes. Ou serializar um arquivo de duas formas diferentes! Ou invalidar cache de três formas diferentes! Em qualquer situação assim, onde você se imaginar fazendo um if para escolher qual algoritmo usar para fazer uma ação, você pode aplicar o padrão Strategy!

Temos três estratégias, definidas por uma interface, compostas em uma classe!
Instancie a sua classe compondo-a com algo que dê a ela a estratégia de que precisa para resolver um problema. Isso é a estratégia! É só um nome para o que fizemos na aula anterior!

## Mais Padrões de projetos
Lista de padrões de projeto, adaptada do Refactoring Guru
🧰 Se quiser conhecer outros padrões de projetos, consulte o site Refactoring Guru , uma fonte de conhecimento excelente para se guardar!

## Code Smells
Conforme naturalmente desenvolvemos o nosso código, existem algumas práticas que a princípio podem parecer a melhor forma de resolver o problema, naquele momento, porém trazem problemas eventualmente. Estas práticas acabaram ficando famosas na comunidade de programação, por serem coisas que acontecem muito. Foram apelidados de "code smells"; maus cheiros no código, indicando que algo está errado, embora possa não parecer de imediato.

Reconhecer estas práticas é importante para que possamos identificá-las em nosso código, e assim evitar problemas e dificuldades. Você já deve ter se deparado com alguns deles, só não sabe ainda seus nomes:
Long Method : métodos grandes geralmente significam mais de uma responsabilidade em um mesmo trecho de código. Por isso, como regra geral, métodos não devem ser muito longos;
Large Class : classes grandes geralmente significam mais de uma responsabilidade. Por isso, como regra geral, classes não devem ser muito grandes;
Duplicate Code : códigos duplicados geralmente significam falta de abstração, ou seja, lógica repetida que poderia estar centralizada em uma única entidade compartilhada. Assim sendo, uma aplicação não deve ter trechos de código duplicados;
Dead Code : se um código não está mais sendo utilizado, porque ainda está lá?
Speculative Generality : quem nunca tentou adivinhar o futuro e tornou uma implementação mais complicada do que precisava? Essa aqui é extremamente comum de fazermos sem perceber!
Vamos dar uma olhada em mais alguns exemplos!

## Data Clamps

Ocorre quando um grupo de variáveis (como o endereço de entrega do exemplo que veremos abaixo) é passado junto como parâmetro em várias partes do programa. É indicativo de que esses grupos devem ser transformados em suas próprias classes.

Exemplo:
Imagine que você tem um aplicativo para uma hamburgueria local, que só faz entregas na própria cidade. Nesta plataforma queremos registrar uma pessoa com seu nome e endereço para facilitar as entregas.

class User:

    def __init__(self, name, street, number, district):
        '''Você nunca vai passar a rua sem passar também o número e o bairro!'''
        self.name = name
        self.address_street = street
        self.address_number = number
        self.address_district = district

Solução

class Address:
    def __init__(self, street, number, district):
        '''As informações que nunca vem separadas são uma entidade separada agora.'''
        self.street = street
        self.number = number
        self.district = district

class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address

Se você sabe que essas informações vão servir exclusivamente para leitura e nunca vão ser alterados diretamente, o Python tem uma solução super simples para elas: namedtuple .

from collections import namedtuple

GeoPoint = namedtuple('GeoPoint', 'lat lon')
location = GeoPoint(-22.81711234090266, -47.069559317039655)
print(location.lat) # muito melhor do que location[0]

## Middle Man

Se uma classe somente delega uma ação para outra, por que deveria existir? Corte o intermediário!
Exemplo:
Temos uma plataforma onde a pessoa jogadora (Player) possui jogos (PlayerGame) e participa de torneios (Tournaments). Nesta plataforma temos um cliente que precisa consultar os torneios de poker de uma pessoa jogadora. Para fins desse exemplo utilizaremos a pessoa jogadora com id 1 e o jogo de poker que ela comprou também com id 1.

class Player:
    # ...

    def game(self, game_id):
        '''Busca um jogo da pessoa através do seu id'''
        return PlayerGame.query.filter(game_id=game_id, user_id=self.id).first()

    def tournaments(self, game_id):
        '''Aqui estamos buscando pelos jogos de uma pessoa para encontrar
        seus torneios.

        Ou seja, usamos o middle man PlayerGame para encontrar o torneio.
        O que além de adicionar complexidade de código, adiciona uma consulta
        extra ao banco de dados.
        '''
        return self.game(game_id).tournaments()


class PlayerGame:

    def tournaments(self):
        return Tournament.query.filter(game_id=self.game_id).all()


class Tournament:
    ...


# Código cliente
player = Player(id=1)
print(player.tournaments(1))

Solução

class Player:

    # ...

    def tournaments(self, game_id):
        '''Aqui removemos o middle man PlayerGame da consulta,
        fazendo-a diretamente em Tournament.

        Com isso simplificamos o nosso código e removemos uma consulta.
        '''
        return Tournament.query.filter(game_id=game_id, user_id=self.id).all()


class Tournament:
    ...


# Código cliente
player = Player(id=1)
print(player.tournaments(1))

Se quiser conhecer mais code smells, consulte o Refactoring Guru ! E não deixe de conferir também... as regras do seu linter ! Elas buscam code smells e impedem a gente de deixá-los em nosso código!


### Adapter