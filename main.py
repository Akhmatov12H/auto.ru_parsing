from selenium import webdriver
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["ru-RU", "ru"], # Лучше поставить ru, так как сайт российский
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://auto.ru/krasnodar/cars/daewoo/all/"
driver.get(url)

# Ждем, пока страница полностью прогрузится
time.sleep(15) 

# 1. Забираем HTML-код прогруженной страницы
html = driver.page_source

# 2. Создаем объект BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 3. Закрываем браузер (данные уже у нас в переменной soup)
driver.quit()

# 4. Ищем объявления
# На Auto.ru карточки машин обычно имеют класс 'ListingItem'
cards = soup.find_all('div', class_='ListingItemTitle')

print(f"Найдено машин на странице: {len(cards)}")
print("-" * 50)

for card in cards:
    try:
        # Ищем название (ссылку внутри карточки)
        title_element = card.find('a', class_='ListingItemTitle__link')

        
        if title_element:
            name = title_element.text.strip()
            link = title_element['href']
            
            print(f"Машина: {name}")
            print(f"Ссылка: {link}")
            print("-" * 20)
    except Exception as e:
        continue
