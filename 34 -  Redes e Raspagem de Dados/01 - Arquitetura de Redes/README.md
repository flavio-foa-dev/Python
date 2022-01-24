# Arquitetura de Redest
## O que vamos aprender

no conteudo de hoje iremos nos aprofundar  mais em redes de computadores, entendendo um pouco melhor como funcionam as diversas redes e como utilizamos isso no nosso dia a dia, seja para acessar uma aplicação ou para desenvolver uma aplicação que explore essa arquitetura. Aprendemos tambem sobre os diversos protocolos e como eles são utilizados,
assim como os diversos componentes que formam as redes de computadores como, por exemplo, clientes e servers.

Antes, no entanto, de começarmos a falar sobre rede computadores e sua arquitetura precisamos falar sobre a internet, a rede mundial de computadores que permitem a troca de informações globalmente. A internet nada maius é que uma implementação de uma rede gingatesca de computadores mmanipuladas pelos gorvernos

## sera capaz de:

- Entender um pouco mais como funciona a internet
- Conhecer os conceitos basicos de redes de computadores
- Entender os modelos de cliente-servidor e p2p
- Entender como funciona a estrutura de camadas nas redes
- Conhecer as camadas que formam o principil modelo de rede
- Aprender o que são os protocolos e como os utilizamos no nosso dia a dia

## Isso é importante para

No início de nossa jornada aprendemos alguns conceitos básicos de como funciona a internet. Esses conceitos nos acompanharam durante os outros conteúdos e foram fundamentais para aprendê-los. Ao longo dessa jornada utilizamos os conceitos de cliente-servidor para desenvolvermos servidores NodeJS ou páginas React , onde era possível consumí-las pelo navegador; utilizamos os conceitos do protocolo HTTP ao trafegar dados e ao explorá-los utilizamos o REST com Express .
O conteúdo de hoje será para aumentarmos nossa bagagem sobre esses assuntos, aprofundando um pouco mais no tema para que possamos utilizá-lo de maneira ainda mais efetiva no nosso dia-a-dia, já que estamos em um mundo cada vez mais conectado.
Estamos em um momento em que mais pessoas estão tendo acesso a internet, assim como cada vez mais dispositivos estão sendo criados para se comunicar através dessas redes. Temos computadores, celulares, fones, relógios, carros e até geladeiras capazes de se comunicar através de redes e tudo isso é possível porque todos eles são capazes de "falar a mesma língua", seguindo padrões que permitem a comunicação e troca de informações entre eles.
Antes de iniciar os estudos, um aviso: o conteúdo é desafiador de uma forma diferente da que estamos acostumados. Queremos entender o fluxo de como a arquitetura de redes funciona, então o mais importante aqui não são os códigos, mas sim entender o que eles estão fazendo. Todos códigos estão aqui para nos ajudar a entender os conceitos de redes, pois o código em si nós já conhecemos e o que ainda não soubermos, será demonstrado. Em outras palavras, não se preocupe com o código, mas sim com o conceito passado.

## Internet

Antes do estudo aprofundado, é muito importante conhecer a evolução histórica daquilo que vamos estudar, de forma a ter contexto sobre o assunto. Veja esse vídeo da TecMundo que conta a história da internet!
Você já sabe um pouco sobre redes, seja pelo conteúdo visto nos módulos anteriores, seja por conhecimentos adquiridos ao longo da vida durante o uso de computadores. Vamos rever algumas coisas e nos aprofundar no conteúdo de arquitetura de redes, para que você tenha um entendimento sólido sobre o assunto!

https://www.youtube.com/watch?v=pKxWPo73pX0

## Redes de computadores

Redes de computadores são conjuntos de software e hardware que permitem a comunicação entre diversos dispositivos como computadores, celulares e impressoras, sendo capazes de compartilhar e transmitir dados uns com os outros.
As redes de computadores podem ser de diversos tamanhos. A rede local, por exemplo, interliga os dispositivos em sua casa através de um roteador. Bom, já que pensamos em uma rede pequena, e agora? Qual rede é considerada grande? Oras, que tal uma rede mundial de computadores que liga dispositivos por todo o globo terrestre? 😁
Existe uma classificação quanto a escala dessa rede, sendo que uma rede de escala menor pode fazer parte de uma rede de escala maior:
PAN (Personal Area Network): Chamamos de PAN as redes que abrangem uma pequena área física, com dispositivos que se comunicam de forma bem próxima. Como exemplo, temos a rede que permite que seu fone bluetooth se conecte com seu smartphone ou seu mouse sem fio funcione no seu computador.
LAN (Local Area Network): Rede local de um escritório, casa ou prédio, normalmente abrangendo uma área com algumas salas ou blocos. Interliga computadores, roteadores, smartphones, impressoras, entre outros.
MAN (Metropolitan Area Network): Interliga diversas redes e dispositivos em uma área metropolitana como, por exemplo, vários locais situados em diversos pontos de uma cidade ou bairro. Outra classificação é a NAN (Neighborhood Area Network), que se restringe a uma área de uma bairro ou vizinhança.
WAN (Wide Area Network): Rede geograficamente distribuída, interligando redes e dispositivos em âmbito global (estados, países e continentes). A internet é um exemplo de WAN 😎

As redes são compostas tanto de componentes físicos (hardware) como cabos, roteadores e switches, quanto de softwares que permitem o tráfego de informações.


## Pacotes

Se uma rede de computadores conecta dois ou mais computadores de forma a possibilitar a troca de mensagens, as primeiras perguntas que podem surgir são: quais mensagens são enviadas? quais informações estão contidas nestas mensagens? o que mais é enviado além da informação da aplicação? como é a estrutura da mensagem? como todos os dados são empacotados? Estas perguntas são respondidas com o conceito de pacotes .
Para trafegar uma informação em uma rede, essa informação é convertida para binários e então dividida em diversos pedaços, e esses pedaços são os chamados "pacotes" que são enviados pela rede. Os pacotes possuem diversos dados, além da informação em si, como quem está enviando aquele pacote, qual o seu destino e indicações para que o destinatário saiba se alguma parte da informação se perdeu no caminho e se é necessário solicitar um reenvio, dentre outras funções.
Mas há a pergunta: como devemos adicionar esse monte de informação para enviar os pacotes? E como o outro lado irá saber entender essas informações? Como o outro lado irá juntar cada pedacinho para formar uma coisa só?
Para isso existem os protocolos .

## Protocolos
Temos diversos dispositivos interligados em vários níveis, desde localmente até globalmente, utilizando redes sem fios e cabos. Mas como que essas informações são enviadas, trafegadas e recebidas por outro dispositivos nessas redes? Isso é feito através do que chamamos de protocolos .
Um protocolo é um conjunto de regras e ações a serem tomadas em uma determinada situação.
De maneira semelhante, nas redes de computadores, os protocolos são conjuntos de regras que controlam como os dados são trocados. Dessa forma é possível que, ao enviar um dado (pacote) através da rede seguindo esses padrões, tenhamos a garantia de que os demais dispositivos da rede saberão lê-lo.
Essa padronização é o que permite que diversos dispositivos sejam criados e produzidos a cada dia, todos capazes de se conectarem e trocarem informações com o mundo inteiro através das redes já existentes.
Fazendo uma analogia, quando queremos passar uma mensagem para outra pessoa, a mensagem em si é a informação que queremos passar, as palavras são os pacotes e o idioma é o protocolo. É importante que os computadores estejam "se comunicando no mesmo idioma" e utilizando as palavras adequadamente para que se entendam, da mesma forma que nós humanos precisamos de regras para conseguirmos nos comunicar 😉.

## Modelo de Rede
Existem diversos protocolos, cada um responsável por definir as regras para um objetivo específico. Por exemplo, temos protocolos que definem como o dado será trafegado, outros para definir como traduzir os dados recebidos no pacote.
Essa separação é feita para permitir a modularização, de modo que cada protocolo defina regras específicas para a parte pela qual ele é responsável e para que seja possível utilizar combinações de protocolos de acordo com a nossa necessidade.
Dividimos então os protocolos em grupos, agrupando cada tipo no que chamamos de camadas. Por exemplo, precisamos de uma camada para identificar quem está enviando a informação e pra quem ela se destina, precisamos de outra camada para traduzir os dados a serem trafegados, etc.
Um conjunto dessas camadas forma o que chamamos de modelo, que basicamente define quais as camadas necessárias para a montagem de um pacote.

## Modelo ISO/OSI
O modelo ISO/OSI (em inglês Open Systems Interconnection ), foi lançado com o objetivo de ser um padrão entre os diversos dispositivos de comunicação. Esse modelo divide as redes de computadores em 7 camadas:

Cada camada é responsável pela inserção de uma funcionalidade ao modelo:
1. Física: Estabelece a comunicação entre os dispositivos no sentido físico. Responsável pelo cabeamento, pelas características elétricas como tensão, ópticas (quando se der por meio óptico) ou eletromagnéticas em uma rede sem fio. Tudo isso garantindo que ocorra a transmissão dos dados pelos meios físicos (hardware), sem perder 0 s e 1 s.
2. Enlace: Também chamada de "link de dados", essa camada é responsável pela detecção e eventualmente pela correção de erros que tenham ocorrido no nível físico. Ela também realiza o controle do fluxo da transmissão entre um dispositivo e outro.
3. Rede: Responsável pelo endereçamento dos dispositivos na rede, assim como pela rota (caminho) que os pacotes deverão percorrer para chegarem da origem até destino.
4. Transporte: Responsável pela detecção e correção de erros que tenham ocorrido nas camadas anteriores, assim como pela ordenação, garantindo que os dados saídos da origem sejam os mesmos no destino. Além disso, ela define a conexão que será usada e como estabelecê-la, assim como controla o fluxo e congestionamento de dados.
5. Sessão: Responsável pela comunicação entre dois processos que estão em máquinas diferentes, controlando o status, definindo quando deve começar, terminar ou reiniciar a comunicação entre origem e destino.
6. Apresentação: Responsável pela conversão entre os formatos de caracteres para que possam ser utilizados na transmissão, também responsável pela compressão e criptografia desses dados.
7. Aplicação: Essa camada é responsável pelo controle da sintaxe e da semântica da mensagem, traduzindo de fato as informações trafegadas.
Bastante coisa?! O importante aqui é saber que o dado é encapsulado por essas diversas camadas, como se fossem aquelas "bonecas russas":

A informação passa por uma primeira camada, sendo formatada e tendo informações adicionadas de acordo com sua regra. Em seguida, o resultado desse primeiro encapsulamento é passado para a outra camada, onde a informação é novamente tratada e são adicionadas as informações pertinentes àquela camada. Esse processo é repetido por todas as camadas até que os dados estejam aptos para serem trafegados ao seu destino.
Da maneira inversa, o destinatário realiza o desencapsulamento, compreendendo os dados de cada camada e então prosseguindo para a camada seguinte.

## Modelo Internet - TCP/IP
O modelo ISO/OSI, como o nome já diz, é um "modelo": isso quer dizer que ele define camadas abstratas a serem tratadas. É necessária, portanto, uma implementação que aplique esses conceitos. Uma das implementações desse modelo é a TCP/IP, que é um conjunto de protocolos de comunicação: TCP ( Transmission Control Protocol - Protocolo de Controle de Transmissão) e o IP ( Internet Protocol - Protocolo de Internet).

## O TCP/IP define 4 camadas mesclando as 7 do modelo OSI:

## Aplicação
A camada de aplicação contém os protocolos responsáveis por dar significado às informações, sendo a primeira camada passada para a mensagem.
Como exemplos de protocolos dessa camada temos o SMTP ( Simple Mail Transfer Protocol - Transmissão de e-mails), FTP ( File Transfer Protocol - Transferência de arquivos) e o nosso velho amigo HTTP ( Hypertext Transfer Protocol - Comunicação WEB).
Tomando como exemplo o HTTP, quando subimos um front-end e temos um servidor capaz de servir páginas web, esse processo é realizado utilizando HTTP. Ao subirmos o servidor, o mesmo ficará aguardando por um pedido, por requisições. Quando acessamos aquele serviço pelo navegador, por exemplo, o navegador está fazendo uma chamada HTTP ao servidor, ou seja: o pedido é feito seguindo os padrões desse protocolo, de modo que o servidor saberá como interpretá-lo, processá-lo e devolver a devida resposta. Essa resposta também seguirá as regras do protocolo, de modo que o navegador ( client ) também saiba entender o que foi retornado e, além do conteúdo das páginas (o html , css e o js ), também são entregues na resposta outros dados do protocolo, como os headers .
Dessa mesma forma, outros protocolos podem ser utilizados nessa camada, SMTP, FTP, DHCP, entre outros. Cada um terá suas regras e padrões de modo que, ambos os lados, cliente e servidor, saibam interpretar as informações.

## Transporte

A camada de transporte, como o próprio nome indica, é a camada responsável pela transferência de dados entre diferentes máquinas (seja um servidor ou um computador pessoal). Os principais protocolos dessa camada são o TCP e o UDP .
Os protocolos possuem diferentes aplicabilidades. Por exemplo, para criarmos um servidor para servir uma página web não podemos ter perda de informações, caso contrário a página não chegará por completo a quem pediu. Da mesma forma que, ao construirmos uma API, temos que garantir que os dados enviados, como o conteúdo de um formulário de cadastro, chegue até o servidor, assim como garantir que os dados respondidos em uma consulta feita ao servidor , por exemplo, sejam entregues por inteiro ao cliente que fez essa solicitação. Nesses casos o TCP é o protocolo mais adequado.
Por outro lado, ao assistirmos uma live ou jogarmos algum jogo online, alguns dados podem ser perdidos, por exemplo, parte da transmissão do vídeo, de maneira que perceberemos apenas uma oscilação na transmissão. Nesse caso, o UDP é mais indicado, já que com TCP, caso essa perda de pacote ocorra, será necessário aguardar o reenvio para então ser dado continuidade no processo. Além disso o UDP permitirá uma maior velocidade na transmissão e também que o conteúdo seja transmitido para diversos clientes ao mesmo tempo, permitindo que diversas pessoas assistam àquele conteúdo em tempo real.

## Rede

O principal protocolo utilizado nessa camada é o IP - Internet Protocol , que inclusive dá nome ao modelo. Outras opções de protocolos dessa camada temos o ICMP, NAT, ARP. Todos eles lidam com o endereçamento da comunicação. Mas o que seria o endereçamento?!
Imagine que você vai enviar uma mensagem para alguém através de uma carta. Você então escreve a mensagem em uma folha e a coloca em um envelope. Nesse envelope é necessário que você coloque o endereço para o destinatário a qual você está enviando a mensagem, de modo que seja possível entregá-la. Da mesma maneira você precisa informar o seu endereço para que o destinatário possa enviar uma mensagem de resposta para você.
A camada de rede do TCP/IP é utilizada para isso. Ela irá identificar o remetente e o destinatário para que o pacote possa ser transmitido na rede. Caso queira conhecer um pouco mais sobre o IPv6 assista, como conteúdo extra, ao vídeo: 'Os endereços IP não são todos iguais do NIC.br'

## DNS

Estamos falando constantemente de endereços IP: que toda máquina possui um para poder se comunicar na rede e ao endereçar um pacote nós o utilizamos. Porém, a realidade é que não costumamos ver muitos esses números ao utilizar a internet e você deve estar se perguntando que, se eles são essenciais para se navegar, onde eles ficam?
Nós utilizamos um sistema de nomes para identificar pontos da rede, ao invés de usar números, já que nomes são mais fáceis de serem utilizados por pessoas. Por exemplo: imagine que, para acessar o google.com fosse necessário digitar no navegador "8.8.8.8", ou para acessar o site da Trybe fosse necessário digitar "34.193.204.92". Seria muito complexo e nada fácil, certo? Para simplificar isso existe o sistema de DNS .
Dessa forma, de maneira bem resumida, conseguimos atribuir um "nome" a um endereço IP específico.
### Interface / Acesso ao Meio

Por último, mas não menos importante, temos a camada física ou de abstração do hardware, também chamada de camada de interface ou de acesso ao meio.
A principal função dessa camada é realizar a interface do modelo TCP/IP com os diversos modelos de rede, por exemplo o protocolo Ethernet , transmitindo os dados através dos meios físicos, encontrando e transmitindo tudo pelo melhor caminho possível. Esta camada lida com os meios de comunicação, corresponde ao nível de hardware, ou meio físico, que trata dos sinais eletrônicos, conector, pinagem, níveis de tensão, dimensões físicas, características mecânicas e elétricas, etc.
## Recapitulando

Para recapitular todas as camadas vamos utilizar o exemplo de um front-end, aqueles que fizemos nos conteúdos anteriores e conseguimos acessar pelo navegador. Vamos imaginar que este front-end está publicado em um servidor diferente da nossa máquina.
Ao rodar o projeto é criado um servidor HTTP , ou seja, camada de aplicação do modelo. O navegador entende esse protocolo e, quando tentamos acessar o site pela sua url, é feita uma requisição HTTP ao servidor. Esse nosso "pedido" pelo conteúdo do site é complementado com as informações de controle daquela camada, por exemplo, com os headers e com o método HTTP daquela chamada, no caso um get . Dessa forma o servidor saberá interpretar o que está sendo solicitado.
Antes de enviar essa informação ao servidor, os dados, já dentro do "envelope" do HTTP, passam pela próxima camada, a camada de transporte. A camada de transporte irá estabelecer a conexão com o servidor. No nosso caso, como não podemos ter perda de pacotes na transmissão, utilizamos o protocolo TCP para isso. Os "envelopes" então tem os dados de controle dessa camada adicionados para que o cliente possa avisar ao servidor que será feita uma transmissão e estabelecer a conexão. Além disso, caso a informação seja muito grande, os dados podem ser divididos em vários pacotes. Essa camada também irá colocar informações de controle para que esse "quebra cabeça" seja montado do outro lado.
Depois disso os dados, agora já encapsulados pelas duas camadas anteriores, passam pela camada de rede. Para identificar o remetente e o destinatário, é então utilizado o protocolo IP , adicionando suas informações de controle, como um identificador único para cada um dos lados, de modo que a mensagem possa ser roteada pela internet e entregue ao seu destinatário.
Por último, a mensagem então é encapsulada pela última camada, responsável por "traduzi-la" para os meios físicos, utilizando, por exemplo, o protocolo Ethernet , passando pelo cabeamento do seu computador até o roteador e de lá seguindo várias rotas, cada pacote seguindo por um lado, atravessando bairros, cidades, países e até o oceano até chegar no servidor onde seu site está hospedado.
Chegando lá o mesmo processo é realizado, porém no sentido contrário. Primeiro o pacote deverá ser entendido pela camada física, traduzindo a mensagem entregue pelo hardware.
Em seguida a mensagem é então entregue ao servidor correto, devidamente identificado pela camada de rede e então a informação passa pela camada de transporte, aceitando a conexão solicitada pelo cliente e reorganizando os diversos pacotes que estão chegando. Esses pacotes então, depois de reordenados, são interpretados pela camada de aplicação.
O server então compreende que deve responder com o HTML , o CSS e o JS do site. Então ele pega todo esse conteúdo, encapsula novamente, utilizando o protocolo TCP/IP, passando por todas as camadas novamente e o processo se repete até o seu navegador receber o conteúdo a ser renderizado para carregar a página solicitada.


