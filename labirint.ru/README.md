Вступление
------------
Данный репозиторий содержит тестовые сценарии для интернет-магазина Labirint.ru использованием PageObject
паттерна, Selenium и Python (PyTest + Selenium).

Файлы
-----

[conftest.py](conftest.py) содержит весь необходимый код, чтобы поймать неудачные тестовые случаи и сделать снимок экрана
страницы на случай, если какой-либо тест не удастся.

[pages/base.py](pages/base.py) содержит реализацию шаблона PageObject для Python.

[pages/elements.py](pages/elements.py) содержит вспомогательный класс для определения веб-элементов на веб-страницах.

[tests/test_auth_page.py](tests/test_auth_page.py) содержит тесты авторизации для Labirint.ru (https://www.labirint.ru/)

[tests/test_book_page.py](tests/test_book_page.py) содержит тесты страницы отдельно взятой книги

[tests/test_cart_page.py](tests/test_cart_page.py) содержит тесты корзины

[tests/test_main_page.py](tests/test_main_page.py) содержит тесты главной страницы

[tests/test_search_page.py](tests/test_search_page.py) содержит тесты работы поиска и фильтров

Запуск Теста
----------------

1) Установить все зависимости:

    ```bash
    pip3 install -r requirements
    ```

2) Загрузить Selenium WebDriver  https://chromedriver.chromium.org/downloads (выберите версию, совместимую с вашим браузером)

3) Запуск теста:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```

Замечание:
~/chrome указывает на путь к файлу Selenium WebDriver, загруженному и разархивированному в шаге #2.
