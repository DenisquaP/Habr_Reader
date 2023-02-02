import requests
from bs4 import BeautifulSoup


def verify_url(url):
    habr_start = 'https://habr.com'
    if habr_start not in url and requests.get(url).status_code != 200:
        return False


def parser(url):
    page = requests.get(url)

    html_code = page.text
    soup = BeautifulSoup(html_code, "lxml")

    head = soup.find('h1').text  # File name

    # Removing invalid characters from file`s name
    head = head.translate({ord(i): None for i in "\\/:*?\'\"<>«»|+., "})

    data = soup.find_all('div', class_="tm-article-body")

    # I need text by one string
    text = ''.join([i.text.replace('\n', '') for i in data])

    return text, head  # Return file name
