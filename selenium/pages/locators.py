import os
from pages.base import WebPage
from pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://numatech.ru/'

        super().__init__(web_driver, url)

    # Поле поиска
    search = WebElement(xpath='//input[@name="search"]')
    # Кнопка поиска
    search_run_button = WebElement(xpath='//button[@type="submit"]')
