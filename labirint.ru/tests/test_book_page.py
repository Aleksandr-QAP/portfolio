from pages.labirint import MainPage


def test_buy_book_page(web_browser):
    page = MainPage(web_browser)
    page.book.click()
    page.buy_book_page.click()

    assert page.message_buy_book_page


def test_reserved_book_book_page(web_browser):
    page = MainPage(web_browser)
    page.book.click()
    page.scroll_part_down()
    page.reserved_books_book_page.click()

    assert page.message_reserved_book_book_page


def test_compare_book_book_page(web_browser):
    page = MainPage(web_browser)
    page.book.click()
    page.compare_book_page.click()
    page.compare_book.click()

    assert page.message_compare_book_page
