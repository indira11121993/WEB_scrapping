import bs4
import requests
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-User': '?1',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Cache-Control': 'max-age=0',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Dnt': '1',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://google.com',
    'Pragma': 'no-cache',
}

URL = "https://habr.com"

## Определяем список ключевых слов:
KEYWORDS = ['blender', 'подход', 'Python', 'PyCharm']

## Ваш код

response = requests.get(URL, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')


for article in articles:
    title = article.find("h2").find("span").text
    href = article.find(class_="tm-article-snippet__title-link").attrs['href']
    date = article.find('time').attrs['title']
    previews = article.find(class_="tm-article-body tm-article-snippet__lead").text
    # print(previews)

    for keyword in KEYWORDS:
        pattern = rf'\b{keyword}\b'
        regex = re.search(pattern, previews)

        if regex :
            result = f'<{date}> - <{title}> - <{URL}{href}>'
            print(result)
            break
