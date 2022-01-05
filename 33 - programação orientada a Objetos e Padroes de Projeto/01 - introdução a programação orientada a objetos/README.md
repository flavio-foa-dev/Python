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

### User nossa primeira entidade

O que é a nossa entidade User? É alguém que quer recuperar uma senha por email. Esse alguém, portanto, tem um email e uma senha. Para identificarmos a pessoa, vamos dar um nome também. Por enquanto, parece que é só disso que precisamos. O Python nos dá ferramentas para criar entidades da forma como quisermos! Com o exemplo, vamos conhecer essas ferramentas um pouco melhor.

```
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
```
Pronto, codamos a nossa entidade! 😄
No Python, a palavra reservada class é usada, como você talvez imagine, para definir entidades. Não uma entidade específica, uma pessoa específica, mas a entidade de uma forma um pouco mais abstrata, como vimos acima. "Uma entidade user contém um nome, um email e uma senha". É isso que fizemos aí em cima. Para, a partir dessa definição, criarmos uma entidade, precisamos do código abaixo:

```
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
print(meu_user)
print(meu_user.name)
print(meu_user.email)
print(meu_user.password)
```
Veja só! Você criou uma variável que contém... a entidade! Temos nela os valores, os dados daquela entidade. Já vimos variáveis que são números, que são strings, que são montes de coisas... Pois é! Nossa variável é uma entidade. Só vamos usar o nome que é dado a tais entidades. Nossa variável é um... Objeto!

### Objetos em python
```
class User:
    def __init__(self, name, email, password):
        """ Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python, vamos falar mais
        disso adiante!"""
        self.name = name
        self.email = email
        self.password = password

# Para invocar o método construtor, a sintaxe é NomeDaClasse(parametro 1, parametro 2)
# Repare que o parâmetro self foi pulado -- um detalhe do Python.
meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")

# A variável `meu_user` contém o objeto criado pelo construtor da classe User!
```

Muita calma nessa hora, sintaxe nova é sempre confusa de se absorver. Vamos para um segundo exemplo para elucidar as coisas. Já criamos nossa primeira entidade, agora vamos codar a nossa ação de enviar emails!

```
class User:
    def __init__(self, name, email, password):
        """ Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python, vamos falar mais
        disso adiante!"""
        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        print("Envia email de reset de senha")


meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()
```

Olha que interessante! Se definimos numa classe uma função, podemos chamar ela a partir do objeto que criamos! Quando pedimos para um objeto fazer algo, dizemos que estamos enviando uma mensagem àquele objeto . Atenção para isso! Na essência, toda lógica da orientação a objetos parte do envio de mensagens entre objetos.
No código acima, estamos pedindo para meu_user resetar sua senha! Não nos interessa como a ação será feita, só nos interessa que ela será feita! Imagine duas pessoas escrevendo esse código. A pessoa que cria o objeto e pede que ele resete sua senha não precisa saber como ele faz isso! Temos uma classe bem nomeada, com uma função bem nomeada, e isso basta! Ao invés de gastar tempo precioso entendendo seu código, a pessoa pode usá-lo sem esse esforço!

```
class User:
    # Não preciso saber como a classe funciona, lalalalala

    def reset_password(self):
      # A classe tem essa função? Ótimo! Pra mim basta!


# Já sei o suficiente pra agir!
meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()
```
Beautiful.
Agora pause e imagine uma aplicação com dez entidades. Vinte. Cinquenta. Imagine ter que saber como cada uma funciona para codar e utilizá-las. Agora imagine que basta saber qual função usar e o resto acontece automagicamente? Esse é o poder da Programação Orientada a Objetos! Se você já chamou a função de um Service, numa aplicação MSC , e a usou sem saber como ela estava feita, saiba que, no fundo, o que você fez foi usufruir do benefício da Programação Orientada a Objetos, que embasa o MSC!

Toda arquitetura que tenha como base a Programação Orientada a Objeto quer isso. Quer que você defina entidades e as use sem entender como elas funcionam . Faz sentido? Pois saiba que você acabou de conhecer dois dos quatro pilares da Programação Orientada a Objetos. O pilar de definir entidades chama-se Abstração . O pilar de usá-las sem entender como elas funcionam se chama Encapsulamento .
Mas calma! Antes de continuarmos, vamos parar para tomar nota desse monte de nomes que estamos aprendendo!

### Dicionario de conceitos:
Na Programação Orientada a Objeto muitas coisas tem nome, e é importante sabermos quais são, são jargões importantes para uma boa comunicação no mercado! Vamos parar para resumir tudo o que aprendemos até agora, e dar os nomes ao que fizemos.
