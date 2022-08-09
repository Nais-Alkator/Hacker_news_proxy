# Hacker News Proxy
Локальный прокси-сервер сайта [Hacker News](https://news.ycombinator.com/).

### Принцип работы 
Прокси скачивает страницы вышеуказанного сайта и модифицирует текст на страницах следующим образом: после каждого слова из шести букв стоит значок «™».

### О прокси
Работа прокси-сервера предполагает изменение вашего ip адреса. В виду ряда причин, использование бесплатных ip-адресов неэффективно. Как один из вариантов предлагается установить [HotSpot Shiel](https://www.hotspotshield.com/ru/). Сервис предлагает 500 мб бесплатного трафика ежедневно.

### Запуск проекта с помощью pip
Для работы скрипта необходим установленный интерпретатор Python3. Затем загрузите зависимости с помощью "pip" (либо "pip3", в случае конфликтов с Python2):  

    pip install -r requirements.txt

Запустите команду:

    python manage.py runserver

В браузере перейдите на локальный сервер:

    http://127.0.0.1:8000/

### Запуск проекта с помощью Docker

    docker-compose up

![Иллюстрация к проекту](/screenshot/example.png?raw=true)

Скрипт использует данные из каталогов:
1) `static` - статические файлы.
2) `pages`, в котором хранятся скачиваемые страницы.

### Цель проекта
Подготовка к тестовому заданию.
