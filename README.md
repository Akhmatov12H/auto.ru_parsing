# Программа для парсинга сайта Auto.ru
Она будет написана на python с использованием библиотеки Selenium, Selenium-stealth (requests и beautifulsoup4 устарели на 2026 год). В дальнейшем, собираюсь ввести возможность указания необходимых данных для парсинга, а также возможность развернуть с помощью Docker Compose
Для начала работы с Selenium необходимо скачать библиотеки, а также программу chromewebdriver

Команды для установки необходимых зависимостей:

pip install selenium selenium-stealth webdriver-manager

Также необходимо скачать программу chromiumwebdriver:

wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_win32.zip 

Добавлена возможность для вывода названия и ссылку всех машин любого бренда. Для того, чтобы поменять бренд машины, необходимо вставить url именно того бренда, который вы ищете

url = "https://auto.ru/krasnodar/cars/**Brand_name**/all/"

