from pages.locators import MainPage


def test_search_field(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys("vServer")
    page.search_run_button.click()
    assert page.get_current_url() == 'https://numatech.ru/rezultatyi-poiska?search=vServer'
