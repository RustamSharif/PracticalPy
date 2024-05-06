import requests
from bs4 import BeautifulSoup

# Определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# URL страницы для парсинга
url = 'https://habr.com/ru/articles/'

# Используем requests для получения HTML страницы
response = requests.get(url)
response.raise_for_status()  # Проверяем, что запрос прошел успешно

# Создаем объект BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все статьи
articles = soup.find_all('article')

for article in articles:
    # Извлекаем данные из статьи
    title = article.find('a', class_='tm-article-snippet__title-link').text
    link = 'https://habr.com' + article.find('a', class_='tm-article-snippet__title-link')['href']
    date = article.find('span', class_='tm-article-snippet__datetime-published').text
    preview_text = article.text.lower()

    # Проверяем, содержит ли preview ключевые слова
    if any(keyword in preview_text for keyword in KEYWORDS):
        print(f'{date} – {title} – {link}')