import requests
from bs4 import BeautifulSoup


def parser(url):
    page = requests.get(url)

    # Checking for connection to site
    # Code 200 means successfully connect to site
    if page.status_code == 200:
        html_code = page.text

        soup = BeautifulSoup(html_code, "lxml")

        # File`s name after saving
        head = soup.find('h1').text

        # Removing invalid characters from file`s name
        head = head.translate({ord(i): None for i in "\\/:*?\'\"<>|+., "})
        print(head)

        # Creating file with page`s code
        with open(f'{head}.txt', 'w', encoding='utf8') as file:
            # find_all принимает список со всеми тегами которые он должен найти
            for data in soup.find_all(['p', 'h2', 'ul']):
                file.write(data.text + '\n')

        print('[+] 1/3 taking article from habr')

    else:
        return 'Can`t connect to site, check url'
