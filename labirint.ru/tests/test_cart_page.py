from pages.labirint import MainPage


def test_clear_position(web_browser):
    page = MainPage(web_browser)
    page.scroll_part_down()
    page.book_1.click()
    page.buy.click()
    page.cart.click()
    page.scroll_part_down()
    page.buy_checkbox.click()
    page.cookie.click()
    page.remove.click()

    assert page.message_remove


def test_order(web_browser):
    page = MainPage(web_browser)
    page.scroll_part_down()
    page.book_1.click()
    page.buy.click()
    page.cart.click()
    page.order.click()

    assert page.message_order


def test_order_1(web_browser):
    page = MainPage(web_browser)
    page.scroll_part_down()
    page.book_1.click()
    page.buy.click()
    page.cart.click()
    page.scroll_part_down()
    page.order_1.click()

    assert page.message_order

