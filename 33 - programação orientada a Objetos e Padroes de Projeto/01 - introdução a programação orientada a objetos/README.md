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
### Enviar email - onde eu coloco esta logica ?
Bem!, se temos uma entidade User que quer enviar emais de recuperação de senha, em principios faz sentido que essa entidade saiba enviar emais, certo? Entao bora la ! para uma entidade saber fazer algo, precisamos definir nela uma função que represente essa ação .Algo assim:



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

- Classe :Entidade  "geral que definimos com base no problema que queremos resolver.
- Objeto: Entidade  "Especifica, criada a partidas regras definidas pela entidade "geral". Pense que a classe é o molde e o objeto a escultura que o malde faz!
- Instância: esse é  novo! quando criamos um objeto a parti de uma classe! Dizemos que esse objeto é uma instancia dessa classe! ou, tambem, dizemos que a classe instanciou um objeto!
- Atributo: outro novo! Um atributo é uma informação de uma instancia  que vocẽ criou. O nome de um User, por exemplo.
- Mensagem: Forma com que objetos interagem- chamando funções uns dos outros. Um chamado como esse é um envio de mensagem a outro objeto "User, resete sua senha"
- Abstração: Pilar da programação Orientada a Objetos. Se refere a sempre criar entidades que farão as ações que resolverão seu problema.
- Encapsulamento: Pilar da Programação Orientada a Objetos. Se refere a poder  instanciar  uma entidade e enviar mensagens a ela sem saber como ela funciona por dentro

Tá, tá, tá! Certamente tá um tanto confuso ainda! É normal. A gente precisa explorar mais a nossa situação problema pra entender como Programação Orientada a Objetos é, no fim das contas, uma forma de pensar que faz aplicações melhores !

### Mailer - Criando mais Entidades
Tudo muito bem, tudo muito bom, mas ainda precisamos criar a lógica de envio de email, certo? Não se preocupe, nós fizemos ela para você, mas acompanhe porque é importante!
Para codarmos um envio de email vamos usar dois módulos, o ssl e o smtplib . Ambos nos permitirão logar num servidor de emails e, de lá, fazer um envio de forma segura através da rede. Para conseguirmos fazer isso, precisaremos ter em mãos algumas informações: o email enviador, a senha do email enviador, o email que receberá a mensagem, o assunto e o corpo do email. Precisamos dessas informações à disposição, então vamos colocar elas no nosso construtor para, então, criar a lógica da nossa ação:

```
import smtplib
import ssl


class User:
    def __init__(self, name, email, password, from_email, from_password):
        self.name = name
        self.email = email
        self.password = password
        self.from_email = from_email
        self.from_password = from_password

    def reset_password(self):
        """ Só com isso a função não irá funcionar! O email em
        questão não existe e costuma ser necessário configurar
        permissões no servidor de email para o envio ocorrer. Se
        quiser, explore isso como exercício bônus! (Por segurança,
        crie uma nova conta de e-mail para testar).
        Por hora, basta entender a lógica aqui! """

        subject = "Reset your password"
        message = "Instruções para resetar a senha, com o link de resetar"
        body = f"Subject:{subject}\n\n{message}".encode('utf-8')
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=context
        ) as server:
            server.login(self.from_email, self.from_password)
            try:
                server.sendmail(self.from_email, self.email, body)
            except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused):
                raise ValueError


meu_user = User("Valentino Trocatapa",
                "valentino@tinytoons.com",
                "Grana",
                "password_reset@teste.com",
                "myverysafepassword")
meu_user.reset_password()
```
Feitas as devidas configurações no servidor do email essa lógica funciona, mas temos um problema sério aqui! Você sabe dizer qual é?
Leia o código do final. Estamos criando uma entidade (aliás, estamos instânciando um objeto!) User . Para criá-la, estamos passando seu nome, email, senha e... o email de envio de reset de senha e a senha desse email. Se tivermos mil users teremos sempre o mesmo email de reset e a mesma senha! Note como o construtor de User está lotado de atribuições! E cada instância que criarmos vai ter uma cópia das informações do enviador de emails. Pra quê? Pra nada. Não precisamos disso.
Bora arrumar o código então?
Lembre-se do primeiro pilar de POO, a Abstração ! Se uma lógica parece não pertencer a uma entidade, extraia-a para uma outra entidade, ou para uma entidade nova! Sempre comece por aí para organizar o seu código. No nosso caso, que tal criamos um enviador de emails? O nome faz sentido, não faz? O nome mais literal possível que podemos dar para uma entidade que envia emails é Enviador de Emails . Em inglês, Mailer . Então é esse o nome que daremos. Bom!

```
# ...

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Mailer:
    def __init__(self, from_email, from_password, to_email):
        self.from_email = from_email # Email de origem
        self.from_password = from_password # Senha do email de origem
        self.to_email = to_email # Email a receber a mensagem

# ...
```
Beleza! Temos duas de nossas entidades, as classes User e Mailer. Mas pense conosco. Que leitura faz mais sentido?

```
meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()
```
ou
```
meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_mailer = Mailer("password_reset@teste.com", "myverysafepassword", meu_user.email)
meu_mailer.reset_password(meu_user)
```
Ou ainda, pense nas Mensagens . Qual é mais simples? "User, resete sua senha!" ou "Enviador de emails, resete a senha deste User!" . Ambas são corretas, mas a primeira é melhor no Encapsulamento . A pessoa que vai usar o seu código não precisa saber que, por trás dos panos, há uma entidade Mailer trabalhando com você. Na segunda implementação ela precisa saber disso! A primeira alternativa exige que a pessoa saiba menos da sua lógica e, portanto, a encapsula melhor! Sendo assim, nosso exemplo fica assim:

```
import smtplib
import ssl


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        meu_mailer = Mailer("password_reset@teste.com", "myverysafepassword", self.email)
        meu_mailer.send_email("Reset your password", "Instruções para resetar a senha, com o link de resetar")


class Mailer:
    def __init__(self, from_email, from_password, to_email):
        self.from_email = from_email
        self.from_password = from_password
        self.to_email = to_email

    def send_email(self, subject, message):
        body = f"Subject:{subject}\n\n{message}".encode('utf-8')
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=context
        ) as server:
            server.login(self.from_email, self.from_password)
            try:
                server.sendmail(self.from_email, self.to_email, body)
            except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused):
                raise ValueError


meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()
````

Assim resolvemos o nosso problema com o máximo de lógica encapsulada. E ao separarmos as nossas entidades , nós deixamos a entidade Mailer, de quebra, muito mais genérica! Ela não precisa enviar só emails de reset de senha agora. Ela pode enviar quaisquer emails! 🤩

# Mensagens e Métodos

Vamos ao último nome do dia! Cada objeto pode receber mensagens. O meu_user.reset_password() , por exemplo, pode ser lido como "Meu user, resete a sua senha!" . Dentro da classe User , definimos a função reset_password que irá conter a lógica de resetar senha. Quando você manda uma instância de User resetar a senha, essa função sabe o que deve ser feito.
Funções que "respondem mensagens" se chamam Métodos . Usualmente ela será nomeada com um verbo ( 'Reset your password!' vira reset_password , por exemplo).
No contexto de POO, todas as interações são feitas por troca de mensagens! Isso significa que ou você envia uma mensagem para um objeto ou você não faz nada com ele. O bom Encapsulamento faz com que nós só precisemos saber do nome de uma classe e seus métodos para interagir com ela. No Python, mesmo quando você altera um atributo diretamente, por trás dos panos o que ele faz é enviar uma mensagem de atualização para a classe!

### Dicionario de conceitos, Parte  dois

Há várias formas de se resolver um mesmo problema, todas com vantagens e desvantagens. Há várias formas de se dividir um problema em entidades também, e várias podem ser igualmente corretas. Vamos treinar isso bastante ainda, então não se preocupe por estar com dúvidas! O importante é sempre começar do simples e evoluir devagar, refatorando sempre, na medida em que o problema cresce. Tendo os pilares de POO em mente, a sua evolução te levará para um bom caminho!

Exemplo de uma outra forma de resolver o problema do dia, com as classes `User`, `Mailer`, `EmailNotFoundError` e `UserService`
Para rever os conceitos que aprendemos hoje vamos destrinchar esse exemplo!

### Classes
Uma classe  consiste numa especia de molde  para criação  de novos objetos, definindo seus  atributos e métodos comuns que serão utilizados por ele.

Esse molde pode ser utilizado para definições de diferentes tipos de dados. No exemplo ACIMA TEMOS:

- **User**: Representa a entidade que armazenará as informações de uma pessoa usuária;
- **Mailer**: Representa um gerenciador de envio de emails, que pode ser utilizado em qualquer parte do sistema;
- **EmailNotFoundError**: Representa uma exceção customizada, que é lançada pelo gerenciador de envio de emails, caso não seja possível fazer este envio devido a algum dos emails não existir;
- **UserService**: Representa um serviço que implementa as regras de negócio associadas a uma pessoa usuária, como por exemplo, o envio de um email de redefinição de senha para o caso da pessoa ter esquecido sua senha.

Percebeu que as classes podem representar moldes de diversos tipos?
Isso é uma das coisas que nos permite dividir tão bem as responsabilidades ao usar oo.

## Objeto/instancia

Com a classe criada, podemos instanciar um objeto. Instanciar é o ato de criar um novo objeto/instância a partir da classe definida.
Se formos fazer um paralelo, podemos dizer que a classe define os comportamentos e o objeto armazena o estado.
A forma de fazer isso varia de linguagem para linguagem. Observe uma instanciação na prática em Python:

```
mailer = Mailer(
  "app-dev@email.com",
  "123456",
  "user@email.com"
)
```

Nesse exemplo criamos uma instância de um gerenciador de email com as informações passadas por parâmetro.
Atributo
Atributos são onde as informações de uma instância são armazenadas. Eles representam o estado do objeto.
No nosso exemplo as classes armazenam as seguintes informações:
User: Uma instância de User armazena informações de nome, email e senha de cada pessoa usuária da nossa aplicação;
Mailer: Uma instância de Mailer armazena as informações de quem envia e quem recebe o email, seu assunto e seu conteúdo;
EmailNotFoundError: Classes não precisam necessariamente ter atributos. Essa classe por exemplo, apenas representa um tipo de exceção, não definindo nenhum atributo;
UserService: Atributos não precisam armazenar apenas informações de tipos de dados primitivos, podendo armazenar também instâncias de outras classes, ou até mesmo uma classe em si. Nesse caso, uma instância da classe UserService armazena uma instância de uma pessoa usuária e uma classe de gerenciamento de emails.
Método
Métodos são funções que possuem acesso aos dados armazenados em atributos, podendo implementar comportamentos e alterar seus estados.
Como um método realiza uma ação, a utilização de verbos é uma boa prática para nomeá-los. Nomes como redefinir_senha ou reset_password poderiam ser utilizados para um método que implementa o comportamento de redefinição de senha.
Construtor
É um método especial utilizado para inicializar instâncias de uma classe e que pode receber parâmetros usados para definir as informações armazenadas em seus atributos.
O nome e a implementação desse método especial varia de linguagem para linguagem, bem como a forma de invocá-lo.
Abstração - Pilar da Programação Orientada a Objetos
No contexto de orientação a objeto, este conceito está ligado à definição de características de uma classe de forma abstrata, que aqui significa definir uma classe focando nas mensagens que ela responde e nos atributos de que precisa.
Apesar de termos definido o pilar dessa forma, entenda que a palavra abstração pode ser usada em outros contextos, se referindo a outras coisas. É importante não confundir as coisas! No próximo capítulo falaremos mais disso.
Encapsulamento - Pilar da Programação Orientada a Objetos
Encapsulamento se trata de esconder parte da implementação de uma classe, exibindo de forma pública somente aquilo que é necessário para que o cliente consuma sua classe e deixando detalhes da implementação protegidos ou privados. Porém, apesar de darmos nomes a essas restrições de visibilidade, elas podem ser implementadas de diferentes maneiras dependendo de linguagem para linguagem e não necessariamente precisam ter uma palavra-chave associada (como é o caso do Python e do JavaScript, por exemplo).



