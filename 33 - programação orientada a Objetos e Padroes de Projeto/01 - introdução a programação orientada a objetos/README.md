# Introdução  a programação orientada a objetos
### o que vamos estudar :

O poder do python ja esta em suas mãos. Voce te uma segunda linguagem de programação debaixo do braço, em sua caixa de ferramentas, e ja  começou o processo de construir familiaridade com ela. Agora, e continuando nossa jornada pelos fundamentos de assuntos que podem permear muito sua carreira, vamos conversar não so sobre a organização de uma aplicação python, mas sobre a organização da sua forma de pensar em codigo.

Vamos falar de um assunto muito importante no mercado de trabalho e que fundamenta muitos dos conhecimentos que vão adquirir na carreira. Hoje é dia de **Programação Orientada a Objetos**1

### estudaremos:

- Defenir `Programação Orientada a Objetos` como um paradigma de programação que é base para inumeras arquiteturas de software.
- Descrever `Programação Orientada a objetos`, uma `classe`
- Definir, em `programação Orientada a Objetos` um ` construtor`
- Definir, em `Programação Orientada a Objetos` , um `Objeto`
- Definir, em `Programação Orientada a Objetos` , um `Instancia`
- Definir, em `Programação Orientada a Objetos` , um `Atributo`
- Definir, em `Programação Orientada a Objetos` , um `metodo`
- Implementar, em ` python, classe, instancias, Atributos, Metodos` e envio de `mensagens` entre `objetos`
- Descrever, como pilar da `programação Orientada a Objetos`, O `Encapsulamento`- a exposição somente do que é necessario para uso dos objetos de uma classe

### Isso é importante
A Programação Orientada a Objetos é uma das formas mais populares do mundo de se programar, se não for a mais popular. Linguagens de programação como Java, Python, C++, Ruby e a clássica Smalltalk são fortemente voltadas para que se programe de forma orientada a objetos. Até mesmo linguagens como JavaScript, que não abraçam o paradigma completamente, são muito influenciadas por ele. As classes de JavaScript, para dar um exemplo, vem daí.
Mais do que uma forma de organizar código, Programação Orientada a Objetos é uma forma de pensar que fundamenta algumas das arquiteturas de aplicação que vocês já estudaram e tantas outras que podem aparecer para vocês em suas vidas profissionais. Estudá-la fará de você uma pessoa que programa melhor e dará bases para expandir seus conhecimentos em inúmeras direções no futuro.

#### content
Todas essas formas de organizar tem em comum o fato de que você separa a lógica da sua aplicação em entidades : blocos de código bem descritos, com nome e propósito nítidos. Em Python, assim como em inúmeras linguagens de programação, você pode organizar a sua aplicação de várias formas, mas uma organização baseada na criação de entidades é especialmente boa e de uso muito comum no mercado.
Há uma idéia fundamental aí: separar seu código. Separá-lo nessas entidades bem descritas, com nome e responsabilidade definidas. As formas de organização de aplicações que você vem aprendendo até aqui usam essa idéia como inspiração ou base fundamental, e essa idéia fundamental é mais que uma forma de organizar aplicações, é mais que uma arquitetura: é uma forma de organizar a sua forma de pensar . É uma forma de pensar o seu programa. Nós chamamos isso de um paradigma de programação . E essa forma de pensar, esse paradigma tem nome. Chama-se Programação Orientada a Entidades Objetos (POO).

Nesse bloco, vamos aprender os fundamentos desse paradigma e o praticaremos. Inúmeras arquiteturas de software podem ser implementadas de forma orientada a objetos, e entender esse paradigma te ajudará a lidar melhor com todas elas! Afinal de contas, nem sempre você vai lidar com o MSC ( Model-Service-Controller ) no dia a dia. Seja MSC (Model-Service-Controller), MVC (Model-View-Controller), DDD (Domain Driven Design), Clean Code ou tantas outras, no mercado de trabalho você terá que entender como várias arquiteturas funcionam e terá que trabalhar de acordo com o que elas propõem! O que vamos ver aqui é como, na essência , uma enormidade delas funciona quando implementadas junto com Programaçào Orientada a Objetos! Com esse conhecimento, você terá a base para aprender e praticar inúmeras arquiteturas de aplicações!
Pense, também, no Linter que te acompanha desde os primeiros projetos do curso. Várias de suas regras são estabelecidas assim por serem boas práticas . Ao aprendermos a programar de forma Orientada a Objetos , vamos entender e sentir, mais do que nunca, porque muitas coisas são boas práticas . Esse conhecimento tão fundamental, essa prática dessa forma de pensar, vai fazer de você uma pessoa mais produtiva e mais capaz de resolver problemas quebrando-os em pequenos pedaços com pequenas soluções que se juntam num todo.

# Exemplo: recuperação de senha
# Organizando sua logica em entidades.
Não ha forma certa ou errada  de se organizar um codigo. Todas  as suas formas tem seus beneficios e seus custos.Você pode ter feito o exercicio da seção anterior com bastante facilidade ou pode nem ter conseguido fazer direito! vai variar muito de pessoa para pessoa.Quer uma dica ? PAra pensar de forma **Orientada a Objetos**, faça, para cada problema que se resolver , a seguinte pergunta de
 - Quem quer fazer o que e com o que ?
- no caso , um User quer recuperar a senha com seu email, se ppartimos dai, o que temos?
 - Uma entidade User
 - Uma ação ou entidade de enviar emails
 - uma ação ou entidade de recuperar senhas

Bora codar então! "Mas espera " , você diz! "Eu não sei nada ainda! Tá muito vago. Que nomes eu dou pra essas entidades? Eu divido em arquivos? Funções? Como codo uma entidade? Essas ações entram onde? Eu não sei nada ainda!" Calma! Na dúvida, faça algo pequeno funcionar e siga a partir daí, um pequeno passo de cada vez 🙂

