from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_browser):
        url = "https://www.labirint.ru/cabinet/"
        super().__init__(web_browser, url)

    auth_field = WebElement(xpath='/html/body/div[1]/div[1]/div/div/div/div/div[1]/form[1]/div[3]/input')
    auth_btn = WebElement(xpath='//*[@id="g-recap-0-btn"]')
    main_page_btn = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[1]/div/a[1]/span')
    close_btn = WebElement(xpath='//*[@id="auth-success-login"]/input[2]')
    fail = WebElement(xpath='//small[Compare(test(), "Введенного кода не существует") and '
                            '@class="full-input__msg-small js-msg-small""]')
