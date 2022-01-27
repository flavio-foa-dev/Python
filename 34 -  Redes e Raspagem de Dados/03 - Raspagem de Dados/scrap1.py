import requests
from parsel import Selector


def fetch_content(content_url):
    try:
        res = requests.get(content_url)
        res.raise_for_status()
    except requests.HTTPError:
        return ""
    else:
        return res.text


def scrape_author_paths(html_content):
    selector = Selector(html_content)

    result = selector.css(
        "body > div > div:nth-child(2) > div.col-md-8 "
        "span:nth-child(2) > a ::attr(href)"
    ).getall()

    return result


def scrape_country(html_content):
    selector = Selector(html_content)

    result = selector.css("span.author-born-location ::text").get()

    return result.split(",")[-1]


def scrape_next_page(html_content):
    selector = Selector(html_content)

    result = selector.css("li.next a ::attr(href)").get()

    return result


if __name__ == "__main__":
    quotes_base_url = "https://quotes.toscrape.com/page/9/"
    quotes_html = fetch_content(quotes_base_url)
    author_paths = set(scrape_author_paths(quotes_html))

    next_page_link = scrape_next_page(quotes_html)
    print(next_page_link)

    # countries = []
    # for path in author_paths:
    #     author_content_html = fetch_content(quotes_base_url + path)
    #     author_country = scrape_country(author_content_html)
    #     countries.append(author_country)
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
