from pages.labirint import MainPage
from selenium.webdriver import ActionChains


def test_shipping_and_payment(web_browser):
    page = MainPage(web_browser)
    page.shipping_and_payment.click()

    assert page.get_current_url() == 'https://www.labirint.ru/help/'


def test_certificates(web_browser):
    page = MainPage(web_browser)
    page.certificates.click()

    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'


def test_ratings(web_browser):
    page = MainPage(web_browser)
    page.ratings.click()

    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'


def test_novelty(web_browser):
    page = MainPage(web_browser)
    page.novelty.click()

    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


def test_discounts(web_browser):
    page = MainPage(web_browser)
    page.discounts.click()

    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&' \
                                     'paperbooks=1&ebooks=1&otherbooks=1'


def test_contact(web_browser):
    page = MainPage(web_browser)
    page.contact.click()

    assert page.get_current_url() == 'https://www.labirint.ru/contact/'


def test_support(web_browser):
    page = MainPage(web_browser)
    page.support.click()

    assert page.get_current_url() == 'https://www.labirint.ru/support/'


def test_pick_up_points(web_browser):
    page = MainPage(web_browser)
    page.pick_up_points.click()

    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


def test_change_region(web_browser):
    page = MainPage(web_browser)
    page.region.click()
    page.field_region.send_keys("Санкт-Петербург")
    page.region_click.click()

    assert page.message_region


def test_page_of_reserved_books(web_browser):
    page = MainPage(web_browser)
    page.page_of_reserved_books.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


def test_cart(web_browser):
    page = MainPage(web_browser)
    page.cart.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cart/'


def test_social_vk(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background b-header-b-social-e-icon-m-vk"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://vk.com/labirint_ru'


def test_social_instagram(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background b-header-b-social-e-icon-m-inst"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.instagram.com/labirintru/'


def test_social_youtube(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background b-header-b-social-e-icon-m-yt"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


def test_social_facebook(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background b-header-b-social-e-icon-m-fb"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.facebook.com/labirintru'


def test_social_ok(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background b-header-b-social-e-icon-m-ok"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://ok.ru/labirintru'


def test_social_twitter(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background b-header-b-social-e-icon-m-tw"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://twitter.com/labirint_ru'


def test_social_instagram_child(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background '
                                                       'b-header-b-social-e-icon-m-inst-children"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.instagram.com/labirintdeti/'


def test_social_vk_child(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background '
                                                       'b-header-b-social-e-icon-m-vk-children"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://vk.com/labirintdeti'


def test_social_zen(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background b-header-b-social-e-icon-m-zen"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


def test_social_telegram(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background b-header-b-social-e-icon-m-tg"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://t.me/labirintru'


def test_social_tiktok(web_browser):
    page = MainPage(web_browser)
    menu = web_browser.find_element_by_xpath('//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
                                             'b-header-b-social-e-icon-m-labirint"]')
    hidden_submenu = web_browser.find_element_by_xpath('//*[@class="b-header-b-social-e-icon '
                                                       'b-header-e-sprite-background '
                                                       'b-header-b-social-e-icon-m-tiktok"]')

    actions = ActionChains(web_browser)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.tiktok.com/@labirintru?'


def test_social_vk_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_vk_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://vk.com/labirint_ru'


def test_social_vk_child_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_vk_child_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://vk.com/labirintdeti'


def test_social_youtube_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_youtube_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


def test_social_instagram_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_instagram_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.instagram.com/labirintru/'


def test_social_instagram_child_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_instagram_child_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.instagram.com/labirintdeti/'


def test_social_facebook_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_facebook_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.facebook.com/labirintru'


def test_social_ok_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_ok_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://ok.ru/labirintru'


def test_social_twitter_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_twitter_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://twitter.com/labirint_ru'


def test_social_zen_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_zen_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


def test_social_telegram_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_telegram_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://t.me/labirintru'


def test_social_tiktok_f(web_browser):
    page = MainPage(web_browser)
    page.scroll()
    page.social_tiktok_f.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.message_tiktok


def test_buy_main_page(web_browser):
    page = MainPage(web_browser)
    page.scroll_part_down()
    page.buy.click()

    assert page.message_buy


def test_reserved_book_main_page(web_browser):
    page = MainPage(web_browser)
    page.scroll_part_down()
    page.reserved_books.click()

    assert page.message_reserved_book


def test_compare_book_main_page(web_browser):
    page = MainPage(web_browser)
    page.scroll_part_down()
    page.scroll_part_down()
    page.more.click()
    page.compare.click()
    page.compare.click()

    assert page.message_compare


def test_opening_book_page_from_main_page(web_browser):
    page = MainPage(web_browser)
    page.book.click()

    assert page.message_book


def test_more_books_with_discounts(web_browser):
    page = MainPage(web_browser)
    page.scroll_part_down()
    page.more_books_with_discounts.click()

    assert page.get_current_url() == 'https://www.labirint.ru/best/sale/'
