# Redes de computadores, ferramenta e segurança
## O que vamos aprender

neste conteudo abordaremos conceitos ja vistos nas aulas anteriores com uma pespequitiva de segurança, Iremos conhecer algumas ferramentas, recursos e conceitos que nos possibilitam agregar segurança a nossa aplicação nas diversas redes as quais elas pertecem, incluido na internet

## Voce aprendera será capaz de:

- Entender o funcionamento de ataques como o DDoS
- Entender o que é e como realiza uma conexão segura utilizando SSH
- Entender o que são certificados e como a criptografia é utilizada na internet;
- Entender o que são proxies;
- Entender o que é e como utilizar um firewall
- Gerenciar regras no firewall  padrão do linux

## Por que isso é importante?
Já somos capazes de desenvolver aplicações com front-end e back-end para diferentes propósitos, utilizando diversos recursos. Além disso, já somos capazes de publicar essas aplicações também!
Na última aula, vimos como funcionam as redes de computadores e a internet, com seus protocolos e modelos que permitem que qualquer pessoa, de sua casa, troque informações com outras pessoas de vários lugares do mundo, de maneira fácil e rápida.
Seguindo a mesma ideia, quando publicamos um site, uma plataforma ou um conteúdo na internet, estamos tornando-o acessível ao mundo inteiro. Isso é incrível não é?!
Porém, temos que lembrar que nem todas as pessoas na internet são bem intencionadas e, ao tornar algo público na internet, seja um site ou um servidor, expomos esse algo a essas pessoas.

Mas calma! Essas questões já são alvo de diversos estudos e existem diversos padrões, protocolos e ferramentas que nos ajudam a ter uma boa experiência na internet, contribuindo com a nossa segurança, dos nossos dados e das nossas aplicações.
A criptografia e a segurança na comunicação é assunto de interesse e estudos desde os primórdios da computação. Para nós, que lidamos com o desenvolvimento e manutenção de sistemas, é fundamental conhecer a tecnologia que garante essas qualidades.
Afinal, ao prover segurança em nossas aplicações, também geramos confiança às pessoas que irão utilizá-la: imagine que você criou um e-commerce : as pessoas irão fornecer dados pessoais extremamente sensíveis para efetuar compras nele, como CPF e o número do cartão de crédito. Dessa maneira, elas precisam se sentir seguras para utilizar a plataforma. Além de toda a segurança que precisamos pensar para manipular, armazenar e processar os dados fornecidos, também precisamos ter os cuidados para que uma pessoa mal intencionada não intercepte a comunicação entre a aplicação cliente e nossos servidores e cause algum problema.
Dessa forma, saber utilizar e explicar o funcionamento de um certificado, uma criptografia ou uma ferramenta que seja capaz de nos dar uma camada a mais de segurança é fundamental!

## Protocolos seguros

na ultima aula apredemos  o que são os protocolos e quais são os principais e como eles são utilizados nas redes na arquitetura TCP/IP.

Hoje vamos aprender sobre os protocolos HTTPS, SSH, TLS e SSL, que são protocolos projetados para fornecer segurança.

SSL/TLS e HTTPS

Tanto o SSL (Secure Sockets Layer) quando o TLS ( Transport Layer Security ) são protocolos que implementam uma camada(layer) de segurançla na rede, sendo o TLS o sucessor do SSL(simplificadamente). Ja o HTTPS(Hyper Text Tranfer protocol Secure) nada mais é do que o protocolo HTTP, que vimos anteriomente, com uma camada adicional de segurança utilizando o protocolo SSL/TLS.

Utilizando certificados de segurança com os protocolos HTTPS e TLS, conseguimos fornecer um ambiente muito mais seguro para publicar nossas aplicações na internet, transmitindo confiança às pessoas que as utilizarão e aumentando sua segurança. Com esses protocolos conseguimos garantir que somos quem somos e também que estamos de fato nos comunicando com quem queremos, evitando que alguém se passe por um dos lados da comunicação ou intercepte nossas conexões.
Graças aos avanços que tivemos a partir dos estudos dos algoritmos de criptografia, hoje conseguimos realizar diversos tipos de transações com segurança na internet. Outro exemplo legal de utilização desses protocolos ocorre em nosso dia-a-dia ao clonarmos um repositório do git. Quando queremos trocar dados entre nossa máquina e o servidor, podemos fazê-lo utilizando tanto via HTTPS como através de SSH, utilizando as chaves SSH.

## Firewall e Proxy
Agora que já sabemos como lidar com certificados e com alguns dos principais protocolos de segurança para a internet, vamos ver outro problema bem comum que podemos enfrentar.

## DoS DDoS

Imagine que temos uma aplicação publicada. Estamos utilizando as melhores práticas de desenvolvimento e também já estamos utilizando um certificado e o protocolo HTTPS.
Nosso site está hospedado em um servidor, um computador com memória, processador, disco, enfim. Esses recursos, como sabemos, são limitados, como com qualquer máquina. Nossa aplicação, porém, recebe relativamente poucos acessos por dia e esses recursos são o suficiente para ela funcionar normalmente.
Entretanto, nossa aplicação está publicada na internet e, dessa forma, exposta ao mundo inteiro. Então vamos imaginar que mais uma vez uma pessoa mal intencionada resolva "bombardear" nossa aplicação com diversos acessos simultâneos. Isso pode ser feito de diversas maneiras, e esse ataque é chamado de DDoS ( Distributed Denial of Service ), ou ataque distribuído de negação de serviço. Esse ataque tem como objetivo tirar o serviço do ar, tornando-o temporariamente indisponível.
O gif abaixo exemplifica bem o conceito desse ataque:

Um exemplo desse ataque foi o sofrido pelo github em 2018 , considerado um dos maiores já registrados. Para se ter uma ideia, foram 1,35 terabit recebidos por segundo de tráfego, porém, devido a infraestrutura, o serviço só ficou fora por cerca de 10 minutos e, depois, sofreu algumas instabilidades ao longo do dia.
O gif abaixo exemplifica como um ataque desses acontecem, utilizando diversas máquinas para enviar tráfego para alguns servidores:

Precisamos, também, estar atentos contra esse tipo de ataque. Provavelmente não teremos que lidar com ataques de terabits, porém, aplicações menores utilizam máquinas menores. Assim sendo, nesses cenários há menos capacidade para enfrentar esse tipo de ataque, tendo a possibilidade de ficarem indisponíveis com ataques de escala bem menores do que este que estamos utilizando de exemplo

## Brute Force
Um outro ataque ao qual podemos estar vulneráveis é o conhecido como "brute force", ou ataque de "força bruta", onde indivíduos, robôs ou scripts maliciosos que tentam diversas combinações de usuário e senha, por exemplo, com o objetivo de encontrar as corretas e acessar indevidamente um sistema. Existem diversos métodos de tornar esse ataque mais efetivo. Por exemplo, o uso de listas de palavras com senhas e usuários comuns, tal como usuário "admin" e senha "123456" (por incrível que pareça as pessoas utilizam esse tipo de senha fraca até hoje).
Além de sempre utilizarmos senhas fortes e outros métodos de segurança pessoais com os nossos logins (uso de segundo fator de autenticação e outros cuidados com as senhas), podemos também configurar camadas de proteção extra em nossos servidores para mitigar essas vulnerabilidades.
Agora que já entendemos um pouco dos riscos e a importância da nossa atenção para isso, vamos ver como podemos proteger nossa aplicação contra esses ataques. É aqui que entram os firewalls!

## O que são firewalls?

Firewall, em uma tradução mais livre, significa muro de fogo, ou porta corta fogo, aquelas portas "de escada", utilizadas para evitar a passagem de fogo em caso de incêndios. De maneira semelhante, os firewalls são responsáveis por impedir ou permitir a passagem de determinados tráfegos em uma rede, seja de entrada ou saída.

## Iptables e Netfilter
Na maioria dos sistemas operacionais existem subsistemas de filtragem de pacotes e ferramentas para gerenciamento de firewall. O sistema padrão para filtragem de pacotes do linux é o Netfilter . Existe uma ferramenta utilizada para configurar o Netfilter chamada Iptables , que opera nas camadas 2 e 3 do modelo OSI. O Iptables é, então, o firewall padrão do linux e está presente na maioria das distros.
Como funciona o Iptables?
Ele compara o tráfego de rede que recebe ou envia com um conjunto de regras pré estabelecidas. Essas regras definem as características que um pacote deve possuir e a ação que deve ser tomada para esse tipo de pacote. Podemos criar regras por protocolo, porta de origem/destino, endereço IP, entre outros. Quando ocorre a correspondência de um pacote a uma característica estabelecida em uma regra é então tomada a ação, que pode ser, por exemplo, se aquele pacote será aceito, rejeitado ou registrado em um arquivo de log.
Como diz o próprio nome, a arquitetura do Iptables é formada por "tabelas". Essas tabelas também são conhecidas como cadeias e cada uma possui tipos de regras específicas. Por exemplo, a cadeia "filter" que possui todas políticas (regras) responsáveis por controlar o tráfego que entra ou sai do computador.

## Fail2ban
O fail2ban é um IPS ( Intrusion Prevention System - Sistema de Prevenção de intrusos). Essa ferramenta, de maneira simples, monitora os logs da rede e, de maneira proativa, ao detectar comportamento suspeito, como diversas requisições de um mesmo IP ou diversas tentativas de login SSH, ele criar regras noiptables , de modo a rejeitar aquele endereço de IP específico por determinado tempo.