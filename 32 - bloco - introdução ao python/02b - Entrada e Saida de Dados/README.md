### Entrada e saida em python
### O que vamos aprender ?
Hoje, vamos aprender a estruturar um projeto Python, adicionando  um novo elemento aos nossos programas. Aprederemos como adicionar entrada e saida  de dados e manipular  alguns tipos de arquivos, como csv e json.  Assim poderemos persistir dados.

**Você sera capaz de:**
 - Preparar um ambiente de projeto em Python, definido sua  estrutura de diretórios  e criando ambiente isolados;
 - Instalar bibliotecas de terceiros num projeto Python;
 - Entender como lidar com exceções em python;
 - Receber dados de pessoas usuarias, assim como envialas de volta;
 - Ler e escrever arquivos no formato tabular `csv` === "separados por vigulas"
 - Serializar e dessearalizar dados no formato `Json`

### Isso é importante para

No dia a dia, podemos encontrar aplicações grandes e complexas, que necessitam de uma estruturação do codigo-fonte. A fim de facilitar a manutenção, é uma boa pratica dividir um programa em arquivos menores. por esse motivo, é importante entender o que são **Modulos e pacotes** e como eles funcionam em uma aplicação

Já os dados, são  uma das coisas mais valiosas para uma empresa, porque  podemos se torna informação. A análise desses dados é cada vez mais decisiva para o sucesso ou fracasso de um negocio. A tomada de decisão pode se embasar em informações relevantes como, por exemplo, o nivel do cliente(CSAT)e o seu custo de aquisição para a empresa(CAC)

Aprendendo a manipular arquivos, poderemos persistir dados, recuperá-los e analisá-los posteriormente. Quando dizemos que vamos persistir dados, significa que iremos armazenar/salvar os dados para serem recuperados quando necessários no futuro.
Vivemos em um mar de informações. Porém afogados na ignorância.
Além disso, integração entre sistemas é algo que uma pessoa programadora provavelmente vai se deparar em algum momento de sua carreira. Por isso, é importante conhecer formatos como o JSON , largamente utilizado para comunicação entre sistemas, e o CSV , amplamente utilizado no contexto da Ciência de Dados

### Estruturando uma aplicação
 - Modulos

Um **modulo* é um arquivo que contem definições e instruções em python. O nome do arquivo é um nome acrescido de `.py.` Dentro de um arquivo python, você pode importa um modulo e ter acesso as suas funçõe e classes, etc.

Em linhas gerais, todo arquivo que é escrito com a linguagem python e com a extenção .py é considerado um modulo.
Observe o arquivo `my_math.py`

```
def sum(a, b):
  return a + b


def pot(a, b):
  return a ** b


print(sum(2, 2))
print(pot(2, 3))
```
Este arquivo é um modulo python, que pode ser executado como scripts, com o comando `python3 my_math_py`. se isso ocorre, o retorno será, em ordem, 4 e 8, devido as chamadas das funções dentro dos metodos `print()`.
Etretanto as funções que criamos neste podem ser reaproveitadas por outros módulos, atraves da declaração`import`
A medida que fomos avançando, esses conceitos ficarão cada vez mais claros.

Pacotes 📦

Pacotes são módulos Python que contêm outros módulos e/ou pacotes , comumente separados por responsabilidades similares. Na prática, um pacote é um diretório que pode conter vários módulos (arquivos de extensão .py ) e/ou outros pacotes .
Exemplo de tipos diferentes de imports de pacotes :

```
import http  # importa o pacote http como um módulo

from http import client  # importa o módulo client do pacote http

from http.client import HTTP_PORT  # importa a constante HTTP_POST do módulo client do pacote http
```
tudo isso ficara mais perceptivel, a medida que fomos avançando no conteudo.

### Ambiente virtual

Imagine que , em uma maquina, ha um projeto Python que tem alguns pacotes de terceiros instalados e, dentre eles, ha uma biblioteca na versão 14. imagine também que, na mesma maquina, um novo projeto é iniciado e ele precisa de mesma biblioteca, mais desta vez 2.0 o que fazer? As versçoes são compativeis? se eu atualizar o sistema, a versão antiga vai continuar a funcionar?

O `Venv` entra como resposta a essas perguntas! Ele é um modulo, ja embutido na linguagem, que serve para isolar ambientes entre projetos, Ou seja, eu consigo ter doiius projetos rodando, em dois ambientes diferentes, com versões diferentes de uma mesma biblioteca.

Na pratica, o que vamos fazer é instalar as bibliotecas em um diretório, que esta relacionado ao projeto. Assim, cada projeto pode ter suas propias bibliotecas na versões que quiser. A idéia é a mesma do `npm` no nodeJs

O comando para criação deste ambiente isolado é `python3 -m venv .venv`, sendo que o `.venv` é o nome do ambiente isolado. Este comando deve ser executado na raiz do projeto.

💡 Caso o venv não esteja instalado, utilize o comando `sudo apt install python3-venv `.

Este ambiente isolado será visto como um diretório criado na raiz do projeto. O ponto na frente do nome faz com que o diretório fique oculto.
Depois de criado, temos de ativar este ambiente para usá-lo. Isto é importante, pois sempre que decidirmos trabalhar neste projeto devemos repetir este passo.

 ```
 source .venv/bin/activate
 ```
 Você pode conferir se o comando de ativação do ambiente virtual deu certo com o seguinte comando:
 ```
 which python3
 ```
O resultado será o caminho para a pasta onde você criou seu ambiente virtual ( pwd ), acrescido de .venv/bin/python3 .
Pronto, agora estamos preparados e preparadas para instalar as bibliotecas que precisaremos para nossos projetos.

### Entrada e Saída
De modo geral, podemos dizer que um programa seria menos útil se não pudéssemos coletar valores de pessoas usuárias e muito menos agradável de se utilizar caso o resultado apresentado fosse pouco legível.
Existem algumas maneiras de nos comunicarmos com o exterior do programa em Python para recebermos dados, assim como existem maneiras de melhorar a exibição dos nossos resultados.

### O que vamos aprender
Heje, vamos aprender a estruturar  um projeto Python, adicionando tambem um novo  elemento aos nossos programas . Aprederemos como adicionar entrada e saida de dados e a manipular alguns tipos de arquivos CSV e Json. Assim, poderemos persistir dados.

### Sera capaz de :
- preparar um ambinete em Python, definindo sua estrutura de diretórios e criando ambientes isolados;
- Instalar biblioteca de terceiros num projeto python para
- Entender como lidar com exceções em Python;
- Receber dados de pessoas usuarias, assim como envia-los de volta;
- Ler e escrever arquivos no formato tabular `csv`;
- Serializar e dessearalizar dados no formato `Json`.

### Isso é importante.
No dia a dia, poderemos encontrar aplicações grandes e complexas, que necessitam de uma melhor estruturação do código-fonte. A fim de facilitar a manutenção, é uma boa prática dividir um programa em arquivos menores. Por esse motivo, é importante entender o que são módulos e pacotes e como eles funcionam em uma aplicação.
Já os dados, são uma das coisas mais valiosas para uma empresa, porque podem se tornar informação. A análise desses dados é cada vez mais decisiva para o sucesso ou fracasso de um negócio. A tomada de decisão pode se embasar em informações relevantes como, por exemplo, o nível de satisfação do cliente (CSAT) e o seu custo de aquisição para a empresa (CAC).
Aprendendo a manipular arquivos, poderemos persistir dados, recuperá-los e analisá-los posteriormente. Quando dizemos que vamos persistir dados, significa que iremos armazenar/salvar os dados para serem recuperados quando necessários no futuro.
Vivemos em um mar de informações. Porém afogados na ignorância.

### Entrada e Saída
Funções podem receber argumentos das pessoas que usam o programa, processá-los e retornar algum valor. Mas como estes argumentos chegam a elas? E o resultado do nosso processamento, como exibi-lo para a pessoa utilizando nossa aplicação?
De modo geral, podemos dizer que um programa seria menos útil se não pudéssemos coletar valores de pessoas usuárias e muito menos agradável de se utilizar caso o resultado apresentado fosse pouco legível.
Existem algumas maneiras de nos comunicarmos com o exterior do programa em Python para recebermos dados, assim como existem maneiras de melhorar a exibição dos nossos resultados.

-