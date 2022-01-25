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
