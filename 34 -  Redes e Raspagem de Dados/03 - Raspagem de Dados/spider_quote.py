import requests
import parsel


def fetch_content(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
  except requests.HTTPError:
    return ""
  else:
    return response.text

def extract_quotes(text):
  selector = parsel.Selector(text)
  quotes = []
  for quote in  selector.css('div.quote'):
    text = quote.css("span.text::text").get()
    author = quote.css("small.author::text").get()
    tags = quote.css("a.tag::text").getall()
    quotes.append({
      "text": text,
      "author": author,
      "tags": tags
    })
  return quotes

print("Conteudo correto", fetch_content("http://quotes.toscrape.com/"))
date_site = fetch_content("http://quotes.toscrape.com/")
print(extract_quotes(date_site))