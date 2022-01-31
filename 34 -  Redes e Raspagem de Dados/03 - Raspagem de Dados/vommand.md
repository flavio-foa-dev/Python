python3 -m venv .venv
which python
source .venv/bin/activate
python3 -m pip install requests
python3 -m pip install --upgrade pip

python3 -m pip install parsel
## ele analisa o conteudo HTML



>>> import requests
>>> response = requests.get("http://quotes.toscrape.com")
>>> print(response.status_code)
200
>>> print(response.headers["Content-Type"])
text/html; charset=utf-8

print(response.headers.text)



 python3 -m pip install requests
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

