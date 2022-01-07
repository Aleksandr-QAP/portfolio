from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.labirint import MainPage


def test_search(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()

    assert page.message_search


def test_search_1(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Dtlmvfr')
    page.search_run_button.click()

    assert page.message_search


def test_search_2(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('@%$#%')
    page.search_run_button.click()

    assert page.message_search_1


def test_type(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.sort_products_by_type.click()
    page.paper_books.click()
    page.button_show_type.click()
    element = WebDriverWait(web_browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//div[@data-dir="books"]'))
    )

    assert element


def test_type_1(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.sort_products_by_type.click()
    page.other_books.click()
    page.button_show_type.click()
    element = WebDriverWait(web_browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//div[@data-dir="multimedia"]'))
    )

    assert element


def test_availability(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.sort_products_by_availability.click()
    page.available.click()
    page.button_show_availability.click()
    element = WebDriverWait(web_browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//*[@class="btn buy-link btn-primary"]'))
    )

    assert element


def test_availability_1(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.sort_products_by_availability.click()
    page.preorder.click()
    page.button_show_availability.click()
    element = WebDriverWait(web_browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//*[@class="btn buy-link preorder-link"]'))
    )

    assert element


def test_availability_2(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.sort_products_by_availability.click()
    page.wait.click()
    page.button_show_availability.click()
    page.scroll_part_down()
    element = WebDriverWait(web_browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//*[contains(@text, "ОЖИДАЕТСЯ") and '
                                                      '@class="product-buy buy-not-avaliable fleft"]'))
    )

    assert element


def test_availability_3(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.sort_products_by_availability.click()
    page.no.click()
    page.button_show_availability.click()
    element = WebDriverWait(web_browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//span[text()="Нет в продаже"]'))
    )

    assert element


def test_price(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.sort_products_by_price.click()
    page.with_discounts.click()
    page.button_show_price.click()
    element = WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="price-old"]'))
    )

    assert element


def test_price_1(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.sort_products_by_price.click()
    page.with_cashback.click()
    page.button_show_price.click()
    element = WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="product-cashback"]'))
    )

    assert element


def test_price_2(web_browser):
    page = MainPage(web_browser)
    page.cookie.click()
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.sort_products_by_price.click()
    page.free_delivery.click()
    page.button_show_price.click()
    page.check.click()
    element = WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@title="Бесплатная доставка"]'))
    )

    assert element


def test_all_filter(web_browser):
    page = MainPage(web_browser)
    page.cookie.click()
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.all_filters.click()
    page.all_type_another.click()
    page.all_available_preorder.click()
    page.all_available_wait.click()
    page.all_available_no.click()
    page.all_price.click()
    page.scroll_part_down()
    page.all_price_with_discounts.click()
    page.all_for_whom.click()
    page.all_for_whom_adult_only.click()
    page.all_description.click()
    page.all_description_with_photo.click()
    page.all_show.click()
    page.refresh()
    page.scroll_part_down()
    page.result_all_filter.click()

    assert page.message_all
    assert page.message_all_1
    assert page.message_all_2
    assert page.message_all_3


def test_all_filter_buy_on_book_page(web_browser):
    page = MainPage(web_browser)
    page.cookie.click()
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.all_filters.click()
    page.all_type_another.click()
    page.all_available_preorder.click()
    page.all_available_wait.click()
    page.all_available_no.click()
    page.all_price.click()
    page.scroll_part_down()
    page.all_price_with_discounts.click()
    page.all_for_whom.click()
    page.all_for_whom_adult_only.click()
    page.all_description.click()
    page.all_description_with_photo.click()
    page.all_show.click()
    page.refresh()
    page.scroll_part_down()
    page.result_all_filter.click()
    page.buy_book_page.click()

    assert page.message_buy_book_page


def test_all_filter_reserved_on_book_page(web_browser):
    page = MainPage(web_browser)
    page.cookie.click()
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.all_filters.click()
    page.all_type_another.click()
    page.all_available_preorder.click()
    page.all_available_wait.click()
    page.all_available_no.click()
    page.all_price.click()
    page.scroll_part_down()
    page.all_price_with_discounts.click()
    page.all_for_whom.click()
    page.all_for_whom_adult_only.click()
    page.all_description.click()
    page.all_description_with_photo.click()
    page.all_show.click()
    page.refresh()
    page.scroll_part_down()
    page.result_all_filter.click()
    page.reserved_books_book_page.click()

    assert page.message_reserved_book_book_page


def test_all_filter_compare_on_book_page(web_browser):
    page = MainPage(web_browser)
    page.cookie.click()
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.all_filters.click()
    page.all_type_another.click()
    page.all_available_preorder.click()
    page.all_available_wait.click()
    page.all_available_no.click()
    page.all_price.click()
    page.scroll_part_down()
    page.all_price_with_discounts.click()
    page.all_for_whom.click()
    page.all_for_whom_adult_only.click()
    page.all_description.click()
    page.all_description_with_photo.click()
    page.all_show.click()
    page.refresh()
    page.scroll_part_down()
    page.result_all_filter.click()
    page.compare_book_page.click()
    page.compare_book.click()

    assert page.message_compare_book_page


def test_all_filter_book(web_browser):
    page = MainPage(web_browser)
    page.cookie.click()
    page.search.send_keys('Ведьмак')
    page.search_run_button.click()
    page.all_filters.click()
    page.all_type_another.click()
    page.all_available_preorder.click()
    page.all_available_wait.click()
    page.all_available_no.click()
    page.all_price.click()
    page.scroll_part_down()
    page.all_price_with_discounts.click()
    page.all_for_whom.click()
    page.all_for_whom_adult_only.click()
    page.all_description.click()
    page.all_description_with_photo.click()
    page.all_show.click()
    page.refresh()
    page.scroll_part_down()
    page.result_all_filter_1.click()

    assert page.message_all_book
