from pages.auth_page import AuthPage


def test_auth_page_positive(web_browser):
    page = AuthPage(web_browser)
    page.auth_field.send_keys("Valid_key")
    page.auth_btn.click()
    page.close_btn.click()
    page.main_page_btn.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'


def test_auth_page_negative(web_browser):
    page = AuthPage(web_browser)
    page.auth_field.send_keys("947C-43B6-8BC9")
    page.auth_btn.click()

    assert page.fail
