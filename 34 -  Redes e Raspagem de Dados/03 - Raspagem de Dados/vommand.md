python3 -m venv .venv
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
