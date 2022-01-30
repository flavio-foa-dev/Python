# Raspagem de dados
## O que vamos Aprender
Hoje vamos aprender o que é raspagem de dados e o que podemos fazer utilizando esta técnica. Vamos ver também como fazer requisições web, analisando suas respostas e extraindo dados. Além disso, também vamos ver técnicas para evitar problemas com essa prática.

## Vamos aprender:
- Realizar requisições web;
- Analizar conteúdos HTML afim de extrair dados;
- Aplicar técnicas de raspagem de dados para evitar problemas como bloqueio de acesso;
- Armazenar os dados obitidos em um banco de dados

## Por que isso é importante?

Imagine que você queira fazer comparações de preços e informações, ou talvez descobrir informações sobre algum assunto. Todo o dado a respeito, porem, não esta estruturado, sendo exibido somente uma pagina web. Uma pagina web pode ser util para humanos, mas certamente não util para fazermos analises estruturadas.

A raspagem de dados tem sido muito útil em trabalhos jornalísticos, fornecendo dados para sustentarem matérias, mas também pode ser útil para comparar preços de produtos com a concorrência, automatização de processos maçantes como buscar artigos científicos em bases acadêmicas, recuperação de documentos em sites jurídicos, analisar perfis de redes sociais, recuperar dados públicos do governo e muitos outros lugares.
Caso tenha repetido um processo mais de duas vezes, automatize-o.
Dado a infinidade de usos provavelmente, em sua carreira como pessoa desenvolvedora, você irá se deparar em algum momento com a necessidade de escrever um programa que realize a extração de dados para algum propósito.

## Introdução
Raspagem de dados é uma técnica computacional para extrair dados provenientes de um serviço ou aplicação, estruturando-os em banco de dados, planilhas, ou outros formatos. Consiste em extrair dados de sites e transportá-los para um formato mais simples e maleável para que possam ser analisados e cruzados com mais facilidade.
Alguns passos aplicados nesta técnica são a realização de requisições, análise das resposta e extração dos dados, navegação do conteúdo, limpeza e armazenamento dos dados.
Vamos passo a passo, aprendendo como fazer e prevenindo erros que podem acontecer.

## Requisição web

A comunicação com servidores HTTP e HTTPS se dá através de requisições, em que utilizamos o verbo para indicar que tipo de ação deve ser tomada para um dado recurso. Devemos informar na requisição em qual recurso estamos atuando e no cabeçalho passamos algumas informações que podem ser interessantes como o tipo de resposta aceita ou o tipo de conteúdo sendo enviado.
O Python possui um pacote para lidar com o protocolo HTTP, porém este não é tão amigável para seres humanos. Por isso vamos utilizar a biblioteca requests , que possui uma interface bem mais amigável. Ela pode ser instalada utilizando o comando abaixo, mas lembre-se de criar um ambiente virtual antes de instalar bibliotecas. Para recordar como criar um ambiente isolado, acesse o conteúdo .

 python3 -m pip install requests

 Vamos ver alguns exemplos abaixo de como utilizar a biblioteca requests :


import requests


# Requisição do tipo GET
response = requests.get("https://www.betrybe.com/")
print(response.status_code)  # código de status
print(response.headers["Content-Type"])  # conteúdo no formato html

# Conteúdo recebido da requisição
print(response.text)

# Bytes recebidos como resposta
print(response.content)

# Requisição do tipo post
response = requests.post("http://httpbin.org/post", data="some content")
print(response.text)

# Requisição enviando cabeçalho (header)
response = requests.get("http://httpbin.org/get", headers={"Accept": "application/json"})
print(response.text)

# Requisição a recurso binário
response = requests.get("http://httpbin.org/image/png")
print(response.content)

# Recurso JSON
response = requests.get("http://httpbin.org/get")
# Equivalente ao json.loads(response.content)
print(response.json())

# Podemos também pedir que a resposta lance uma exceção caso o status não seja OK
response = requests.get("http://httpbin.org/status/404")
response.raise_for_status()


## Alguns Problemas

## Rate Limit

Muitas vezes a página de onde estamos removendo o conteúdo possui uma limitação de quantas requisições podemos enviar em um curto período de tempo, evitando assim ataques de negação de serviço.
Isto pode nos levar a ficarmos bloqueados por um curto período de tempo ou até mesmo banidos de acessar um recurso.
Que tal vermos um exemplo?

import requests


# À partir da décima requisição somos bloqueados de acessar o recurso
# Código de status 429: Too Many Requests
for _ in range(15):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(response.status_code)

Neste exemplo, após a décima requisição, o servidor começa a nos retornar respostas com o código de status 429 , "Too Many Requests". Isto significa que estamos utilizando uma taxa de solicitação maior que a suportada. Ele permanecerá assim por algum tempo (1 minuto).

Uma boa prática é sempre colocarmos um uma pausa entre as requisições, ou lote delas, mesmo que o website, onde a informação está, não faça o bloqueio, assim evitamos tirar o site do ar.


import requests
import time


# Coloca uma pausa de 6 segundos a cada requisição
# Obs: este site de exemplo tem um rate limit de 10 requisições por minuto
for _ in range(15):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(response)
    time.sleep(6)


## Timeout
Ás vezes pedimos um recurso ao servidor, mas caso o nosso tráfego de rede esteja lento ou tenha um problema interno do servidor, nossa resposta pode demorar ou até mesmo ficar travada indefinidamente.
Como garantir, após um tempo, que o recurso seja retornado? 🤔

import requests

# Por 10 segundos não temos certeza se a requisição irá retornar
response = requests.get("https://httpbin.org/delay/10")
print(response)

Podemos definir um tempo limite (timeout) para que, após este tempo, possamos tomar alguma atitude como por exemplo, realizar uma nova tentativa.
Este tempo limite normalmente é definido através de experimentações e análise do tempo de resposta normal de uma requisição.

import requests


try:
    # recurso demora muito a responder
    response = requests.get("http://httpbin.org/delay/10", timeout=2)
except requests.ReadTimeout:
    # vamos fazer uma nova requisição
    response = requests.get("http://httpbin.org/delay/1", timeout=2)
finally:
    print(response.status_code)


No exemplo acima, para efeitos didáticos, modificamos a URI do recurso, diminuindo o delay de resposta da requisição, através do timeout , porém normalmente este valor não muda.

## Analizando respostas
🗒 Para realizar a extração de dados de um conteúdo web vamos utilizar uma biblioteca chamada parsel . Ela pode ser instalada com o comando o comando abaixo:

 python3 -m pip install parsel

Como já aprendemos a realizar requisições HTTP e buscar seu conteúdo, vamos agora analisar este conteúdo e extrair informações.
Para ajudar na didática, vamos utilizar o site http://books.toscrape.com/ . Ele é um site próprio para o treinamento de raspagem de dados.
Para começar, vamos acessar o site e ver o seu conteúdo.

Em código, vamos baixar o conteúdo da página e criar um seletor, que será utilizado para realizarmos as extrações. Vamos criar o arquivo .py para buscarmos as informações:
exemplo_scrape.py

from parsel import Selector
import requests


response = requests.get("http://books.toscrape.com/")
selector = Selector(text=response.text)
print(selector)


Ok , que tal extrairmos todos os livros desta primeira página e buscar seus títulos e preços?
Para conseguirmos extrair essas informações precisamos, primeiro, inspecionar cada um dos elementos, buscando algo que os identifique de forma única na página.

    exemplo_scrape.py

# ...


# response = requests.get("http://books.toscrape.com/")
# selector = Selector(text=response.text)

# O título está no atributo title em um elemento âncora (<a>)
# Dentro de um h3 em elementos que possuem classe product_pod
titles = selector.css(".product_pod h3 a::attr(title)").getall()
# Estamos utilizando a::attr(title) para capturar somente o valor contido no texto do seletor

# Os preços estão no texto de uma classe price_color
# Que se encontra dentro da classe .product_price
prices = selector.css(".product_price .price_color::text").getall()

# Combinando tudo podemos buscar os produtos
# em em seguida buscar os valores individualmente
for product in selector.css(".product_pod"):
    title = product.css("h3 a::attr(title)").get()
    price = product.css(".price_color::text").get()
    print(title, price)


O seletor principal que contém todo o conteúdo da página pode ser utilizado em uma busca para encontrar seletores mais específicos. Podemos fazer isto utilizando a função css . Ela recebe um seletor CSS como parâmetro, embora podemos passar um tipo especial de seletor quando queremos algum valor bem específico como o texto ou um atributo.
Após definir o seletor, podemos utilizar a função get para buscar o primeiro seletor/valor que satisfaça aquela busca. A função getall é similar, porém trás todos os valores que satisfaçam aquele seletor.
Assim como temos a função css que faz a busca por seletores CSS, temos também a função xpath que faz a busca com base em XPath.
💡 Existem sites que podem ajudar com seletores css ou xpath .

## recursos Paginados

Tudo certo, temos 20 livros, mas sabemos que na verdade este site possui 1000 livros. que tal coletamos todos

Navegando um pouco por entre as páginas, percebemos que cada página possui uma referência para a próxima. Mas, se a URL é sequencial, por que não simplesmente jogamos valores até a página avisar que o recurso não foi encontrado?
Acontece que podemos evitar fazer requisições desnecessárias, já que a página nos informa a próxima.
O que precisamos fazer é criar um seletor com a página, extrair os dados, buscar a nova página e repetir todo o processo, até termos navegados em todas as páginas.
Até a parte da extração nós já fizemos, vamos então dar uma olhada em como buscar a próxima página.


 exemplo_scrape.py

# ...
# for product in selector.css(".product_pod"):
#     title = product.css("h3 a::attr(title)").get()
#     price = product.css(".price_color::text").get()
#     print(title, price)

# Existe uma classe next, que podemos recuperar a url através do seu elemento âncora
next_page_url = selector.css(".next a::attr(href)").get()
print(next_page_url)

Agora que sabemos como recuperar a próxima página, podemos iniciar na primeira página e continuar buscando livros enquanto uma nova página for encontrada. Cada vez que encontrarmos uma página, extraímos seus dados e continuamos até acabarem as páginas. Então vamos alterar tudo que tínhamos escrito no arquivo exemplo_scrape.py para o código abaixo:
exemplo_scrape.py

from parsel import Selector
import requests


# Define a primeira página como próxima a ter seu conteúdo recuperado
URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html'
while next_page_url:
    # Busca o conteúdo da próxima página
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)
    # Imprime os produtos de uma determinada página
    for product in selector.css(".product_pod"):
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").get()
        print(title, price)
    # Descobre qual é a próxima página
    next_page_url = selector.css(".next a::attr(href)").get()

Nossa, quantos livros! 📚