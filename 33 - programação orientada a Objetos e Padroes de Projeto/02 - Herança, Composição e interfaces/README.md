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

## herança - Especialização de comportamentos
 Não se deve ter medo de criat objetos. Não importa quão pequenos eles sejam, é a separação de responsabilidades que faz o paradigma brilhard

Nós queremos **estender nosso codigo sem modificar o que ja existe**. leia o codigo abaixo! Ele faz a mesma coisa que o codigo anterios, mas esta refatorado. ele usa, para resolver o nosso problema, os conceitos de **classes abstratas, métodos abstratos** e o conceito de **Herança**

from abc import ABC, abstractmethod
import json


class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
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

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)

💡 Como boa prática, cada classe deve ser definida em seu próprio arquivo! Para nossos exercícios isso não é necessário
**Herança** nada mais é do que especializar o comportamento de uma classe. A classe herdeira é tudo que a classe **ascendente** é e um pouco mais! Pense assim:

- Se FileCompressor é a classe ascendente, ZipFileCompressor e TarFileCompressor são classes herdeiras! Ambas são um tipo específico de compressor de arquivos.
- Se DatabaseConnector é a classe ascendente, MySQLConnector e MongoConnector são as classes herdeiras! Ambas são um tipo específico de conector de banco de dados.
- Se Model é a classe ascendente, UserModel é a classe herdeira! É um tipo específico de model .
- Se Service é a classe ascendente, AuthenticationService é a classe herdeira! É um tipo específico de service .
-
💡 Lembre-se: O Model Service Controller é uma arquitetura que usa como base a Programação Orientada a Objetos!

A Programação Orientada a Objetos, portanto, te dá o poder de criar classes herdeiras que especializam, mais e mais, o comportamento das classes ascendentes! Não há limite pra quantidade de classes herdeiras que uma classe pode ter, **mas é crucial que tais classes sempre sejam uma especialização de comportamento!** Já já vamos ver o porquê.

No Python, definimos uma classe como herdeira da outra na linha que a define, como acima em `class SalesReportJSON(SalesReport)` . A lógica é: `class MinhaClasseHerdeira(ClasseAscendente)`

### Exercício de Fixação
2. Antes de prosseguirmos para entender o que é aquele `@abstractmethod` e aquele `(ABC)` , vamos fixar o entendimento de herança! Implemente uma classe `SalesReportCSV` que seja herdeira da classe `SalesReport` , da mesma forma que fizemos com a `SalesReportJSON` . Para testar seu funcionamento, instancie-a e chame sua função `serialize` .

## Classes abstratas
No exemplo acima vimos, alem da herança, outra duas coisas meio confusas! Vimos que a classe acendente principal parece ser herdeira de aoutra, uma tal de classe `ABC`. Alem disso, a função `serializa` da classe ascendente esta marcada como `@abstractmethod` e nao tem codigo algum, ao contrario da classe herdeira. O que raios é isso? 🤔

 Serialize é o processo de mudar o formato dos seus dados para que posam ser amarzenados ou enviados para serem depois, convertidos de volata a sua forma original

Até agora , sempre criamos uma classe para que pudéssemos criar intancias dela para usarmos, não é mesmo? Pois é! Mas pense no exemplo  acima: temos uma classe ascedente "geral a `salesReport` e uma classe herdeira especifica, a `salesReportJSON`. A parti do momento que temos comportamentos gerais e comportamento especializados, **ainda faz entido usar a classe generica ?**. Pensem assim: o relatorio de vendas precisa obrigatoriamente, ter um formato. temos uma classe geral `salesReport` que define comportamentos dos relatorios de vendas e suas classes herdeira especializam na para imprimirem o relatorio em diferentes formatos. **Nos nunca vamos ter um relatorio geral. so um especializado!**

Nesse caso, então, não faz sentido instanciarmos um objeto da `classe SalesReport` . Quando esse é o caso, dizemos que essa é uma **classe abstrata** ! Ou seja: classe abstrata é a classe que não pode ser instanciada nunca! E o `método abstrato` é... a mesma coisa! É um método que nunca pode ser chamado diretamente. A classe `SalesReport` define o método `serialize` para deixar nítido que todo relatório de vendas deve ter uma forma de se serializar, mas ela mesma, por ser geral, não é serializável. Assim sendo, a classe `SalesReport` precisa definir a assinatura do método (nome e parâmetros), mas ele só será chamado sem erros se uma classe herdeira o implementar. **No contexto de Programação Orientada a Objetos, pense que coisas abstratas são coisas criadas para serem especializadas por classes herdeiras!**

### Exercício de Fixação
3. Defina na classe SalesReport um segundo método abstrato chamado get_length que retorna quantos itens tem no relatório. Tente chamar esse método a partir da classe herdeira que não implementa esse método e veja o erro que você recebe. Tente instanciar a SalesReport também! Depois disso, implemente uma lógica qualquer para esse método em uma das classes herdeiras e verifique que já é possível instanciá-la e até chamar o método!

## Interfaces
A Programação Orientada a Objetos dá muitos nomes para as coisas, e agora vamos aprender mais um! No exemplo acima nós definimos uma classe abstrata com um método abstrato . Vemos que a classe a ser especializada, a SalesReport , definiu a assinatura de uma função, mas não a sua lógica! Ou seja: todas as classes herdeiras poderiam colocar ali a lógica que quisessem, contanto que utilizassem a mesma assinatura de função.
Um objeto deve ser capaz de receber mensagens. As funções que você chama são as mensagens enviadas a ele. Quando você dá a um objeto uma função você define uma mensagem que ele será capaz de receber e interpretar. Ao conjunto de mensagens que um objeto pode interpretar é dado o nome de Interface !
Como assim? Pense da seguinte forma: quando duas pessoas de países diferentes conversam, muitas vezes não é possível conversarem em seus idiomas nativos. Pode ser que um Japonês e um Brasileiro, por exemplo, só consigam se comunicar em Inglês. Você só é capaz de se comunicar com a outra pessoa se disser algo que ela é capaz de entender . Com objetos, é a mesma coisa: a interface de um objeto representa o conjunto de mensagens que ele é capaz de entender! Para a classe SalesReport , sua interface é composta pelas funções build e serialize .
Lembra que falamos que uma vantagem da Programação Orientada a Objetos é que só precisamos saber como instanciar um objeto e quais funções ele tem ? Falando a mesma coisa de maneira mais técnica, podemos dizer que a Programação Orientada a Objetos garante interfaces bem definidas para as várias partes do nosso programa se comunicarem sem que se precise saber como, internamente, cada parte funciona . Se suas interfaces tem nomes bons e lógicas bem definidas, fica fácil reusar o código que você escreveu! Não é preciso entender como ele funciona, só como me comunico com ele.

## Dicionário de conceitos

Vamos com calma! Como a Programação Orientada a Objeto tem muitos nomes e conceitos, vamos resumir aqui o que aprendemos até então.

- **Herança** : é uma forma de especializar o comportamento de uma classe com outra classe;
- **Classe Abstrata** : uma classe que não pode ser instanciada. Utilizada para definir as funções comuns (nem sempre abstratas) e suas assinaturas;
- **Métodos Abstratos** : um método, ou função, que precisa ser implementado por uma classe herdeira para funcionar corretamente. Criado para definir uma Interface ;
- **Interface** : conjunto de métodos que um determinado objeto "possui" - ou, o conjunto de mensagens que um objeto é capaz de entender e responder para.

# E quando nem todas as herdeiras vão ter o mesmo comportamento ?
Vamos à mais uma demanda! Os nossos relatórios estão muito grandes, então determina-se que todo relatório deve ser compactado para transitar pelos servidores da empresa! Isso é super importante para economizar rede e disco. Vamos, então, dar aos nossos relatórios a capacidade de se comprimirem!

from abc import ABC, abstractmethod
import gzip
import json


class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
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

    def compress(self):
        binary_content = json.dumps(self.build()).encode('utf-8')

        with gzip.open(self.export_file + '.gz', 'wb') as compressed_file:
            compressed_file.write(binary_content)

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)

class SalesReportCSV(SalesReport):
    # Sua implementação vai aqui
    pass

Repare que adicionamos o comportamento à classe ascendente ! Fazemos isso porque todos os relatórios terão que ser comprimidos. Isso não é um comportamento especializado, é geral! Então faz sentido torná-la parte da interface da classe. E nossa linguagem permite que classes abstratas tenham métodos concretos (ou seja, que fazem coisas de verdade). As classes herdeiras não são obrigadas a re-implementar esses métodos, apenas os abstratos!
Mas bom! Até aí tudo muito bom. Mas chega, um tempo depois, uma nova demanda! "Nossos relatórios estão fazendo um sucesso incrível e agora precisamos que clientes possam baixá-los, compactados, lógico, e descompactá-los! Mas nossos clientes não tem perfil técnico e não vão saber descompactar um arquivo .gz, então é obrigatório nós compactarmos ele em .zip também!"
Você poderia pensar que basta, então, mudar o método .compress() para que compacte em .zip ao invés de .gz mas não! O compactamento do gzip é mais eficiente que o zip . Se mudarmos isso, teremos impacto de custos na nossa infraestrutura e não precisamos disso! Precisamos garantir que todos os relatórios sejam compactados em .zip e em .gz .

Exercício de Fixação
4. Invista cinco minutos tentando resolver esse problema! Spoiler: você encontrará problemas! Quais?

# Composição de - Classes feitas de outras classes

nos ja sabemos que não podemos criar, na classe mãe, uma função `compres_zip` para fazer o que precisamos. se fizessemos isso precisariamos mudar o nome da função `compress` para `compress_gzip`. e como consequencia mudar todos os milhares de lugares onde essa função é chamada.

Pensando como pensamos antes... Poderiamos tentar especializar comportamentos, então? Fazemos uma `salesReportJsonZip` e  uma `salesReportjsonGz, e mesmo pra CSV? mas e os outros formatos de relatorio ? Alem disso, ficamos sabendo que o CTO da empresa esta considerando uma parceria com Winrar........
É, dará ruim. A herança não é o suficiente pra resolver nosso problema. Vamos trazer pro palco, então, outra forma que temos de compartilhar códigos na Programação Orientada a Objetos. A Composição !

from abc import ABC, abstractmethod
import gzip
import json
from zipfile import ZipFile


class ZipCompressor():
    ''' Nossos compressores terão fixado o local de salvamento
    do arquivo, então vamos defini-lo nos construtores'''
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        with ZipFile(file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)


class GzCompressor():
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        with open(file_name, 'rb') as content:
            with gzip.open(file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)


class SalesReport(ABC):
    # Nossa classe agora espera *instâncias* de compressor como um parâmetro.
    # Temos um valor padrão para suportar o código que usava as SalesReport
    # sem parâmetros -- não precisa correr pra re-escrever nada ;)
    def __init__(self, export_file, compressor=GzCompressor()):
        self.export_file = export_file
        self.compressor = compressor

    def build(self):
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

    # Aqui temos um atributo de classe!
    FILE_EXTENSION = ''

    def get_export_file_name(self):
      # Aqui usamos o atributo de classe
      # Vai fazer mais sentido nas classes herdeiras!
      return self.export_file + self.FILE_EXTENSION

    def compress(self):
        self.serialize()
        self.compressor.compress(self.get_export_file_name())

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    # Nós não reimplementamos o get_export_file_name
    # mas como ele usa um atributo de classe pra pegar a extensão
    # só de redefinir o atributo já vamos conseguir mudar o resultado!
    FILE_EXTENSION = '.json'

    def serialize(self):
        with open(self.get_export_file_name(), 'w') as file:
            json.dump(self.build(), file)


class SalesReportCSV(SalesReport):
    # Sua implementação vai aqui
    pass


# Para testar
relatorio_de_compras = SalesReportJSON('meu_relatorio_1')
relatorio_de_vendas = SalesReportJSON('meu_relatorio_2', ZipCompressor())

relatorio_de_compras.compress()
relatorio_de_vendas.compress()



Observe o que fizemos aqui: nós criamos classes próprias para nossos compressores e passamos instâncias delas para nosso relatório! Isso, aliado ao nosso uso de parâmetros nomeados, nos permite, sem mudar código existente algum, dar a cada pessoa o poder de usar nossas classes e escolher se quer usar um compressor .gz , .zip , ou qualquer outro que vier no futuro!
A Herança serve para especializar comportamentos, onde toda classe herdeira deve fazer tudo que a classe ascendente faz . Quando precisamos reusar código, ou os comportamentos começam a aparecer em somente algumas das classes herdeiras, prefira usar Composição ! Aí quem instância a classe escolhe com qual dependência (no nosso caso, o compressor) quer usá-la. O nome disso é Inversão de Dependência 😉. É uma inversão porque não é o autor da SalesReportJSON que define qual classe o método compress vai usar. Quem define é quem cria as instâncias da SalesReportJSON !

## Composição de Interfaces

Nós falamos lá em cima que qualquer outra classe de compressor que surgir funcionará com nosso código! Certo? Observe que, pra isso acontecer, tal classe precisa, necessariamente, implementar a função .compress() com a mesma assinatura que nossas duas classes atuais.
O grande risco que temos ao fazer composição é a classe que passarmos para a outra não ter o mesmo formato que imaginamos! Ou seja: se o nosso novo compressor não tiver uma função chamada compress que receba o mesmo parâmetro que definimos, usá-la dará erro. Como podemos garantir que isso nunca acontecerá? Nós podemos fazer um combinado na empresa mas, já diria o sábio:
Um combinado que não está codado não existe. (Clarice Lispector)
Como a gente coda um combinado ?! A resposta...? Definindo uma interface!
Você, então, dita uma regra: Todo compressor deve ter uma função chamada compress que receba esse parâmetro! E como você faz isso?
Com...


# ...


class Compressor(ABC):
    def __init__(self, filepath='./'):
        self.filepath = filepath

    @abstractmethod
    def compress(self, file_name):
        raise NotImplementedError


class ZipCompressor(Compressor):
    def compress(self, file_name):
        with ZipFile(file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)


class GzCompressor(Compressor):
    def compress(self, file_name):
        with open(file_name, 'rb') as content:
            with gzip.open(file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)

Com uma classe abstrata 😎
Ou seja: todo compressor que for criado precisa ter uma função compress que receberá esse parâmetro específico para funcionar!
Você usa uma classe abstrata com um método abstrato para definir uma interface que, através de herança , definirá o comportamento de todos os compressores futuros, assegurando que sua composição sempre funcionará!


