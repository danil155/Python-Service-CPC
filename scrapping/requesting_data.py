import requests
from bs4 import BeautifulSoup
import re

from config import URL_PIZZA_SCRAP


class PizzaInfo:
    name = str
    price = int
    image = str


def get_info_pizza() -> list:
    response = requests.get(URL_PIZZA_SCRAP)
    if response.status_code != 200:
        print('ERROR in scrapping.requesting_data: there is no connection to the pizzeria website.')
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    data = [text for text in soup.stripped_strings][1:]

    if not data:
        print('ERROR in scrapping.requesting_data: data is empty.')
        return []

    pattern = r'^Пицца\s.+$'

    info = list()

    for index, item in enumerate(data):
        pizza_info = PizzaInfo()
        if re.match(pattern, item):
            if 'Пицца недели' in item:
                continue
            else:
                pizza_info.name = item
                pizza_info.price = data[index + 10]
                info.append(pizza_info)

    images = soup.find_all('img')
    for index, img in enumerate(images[9:]):
        if index >= len(info):
            break
        pizza_info = info[index]
        src = img.get('src')
        if src.find('upload') != -1:
            pizza_info.image = 'https://pizzapizzburg.ru' + src

    return info


if __name__ == '__main__':
    get_info_pizza()


''' # 2. Извлечь все ссылки
print("\nСсылки на странице:\n")
links = soup.find_all('a', href=True)
for link in links:
    href = link['href']
    text = link.get_text(strip=True)
    print(f"Текст: {text}, Ссылка: {href}")

# 3. Извлечь все изображения
print("\nИзображения на странице:\n")
images = soup.find_all('img')
for img in images:
    src = img.get('src')
    alt = img.get('alt', 'Нет описания')
    print(f"Источник: {src}, Описание: {alt}")

# 4. Извлечь таблицы
print("\nТаблицы на странице:\n")
tables = soup.find_all('table')
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all(['td', 'th'])
        row_data = [col.get_text(strip=True) for col in columns]
        print(f"Строка: {row_data}")

# 5. Извлечь списки
print("\nСписки на странице:\n")
lists = soup.find_all(['ul', 'ol'])
for lst in lists:
    items = lst.find_all('li')
    for item in items:
        print(f"Элемент списка: {item.get_text(strip=True)}")'''
