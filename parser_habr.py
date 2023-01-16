import requests
from bs4 import BeautifulSoup


def parser(url):
    if 'https://habr.com' not in url:
        raise ValueError('It isn`t Habr')

    page = requests.get(url)

    # Checking for connection to site
    # Code 200 means successfully connect to site
    if page.status_code == 200:
        html_code = page.text

        soup = BeautifulSoup(html_code, "lxml")

        # File`s name
        head = soup.find('h1').text

        # Removing invalid characters from file`s name
        head = head.translate({ord(i): None for i in "\\/:*?\'\"<>|+., "})

        data = soup.find_all('div', class_="tm-article-body")
        text = ''.join([i.text.replace('\n', '') for i in data])

        return text, head  # Return file name

    else:
        return ''
