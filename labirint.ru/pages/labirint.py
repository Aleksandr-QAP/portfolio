import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # Поле поиска
    search = WebElement(id='search-field')
    # Кнопка поиска
    search_run_button = WebElement(xpath='//button[@type="submit"]')
    message_search = WebElement(xpath='//h1[@class="index-top-title"]')
    message_search_1 = WebElement(xpath='//div[@class="search-error"]')

    # Кнопка отложенных книг
    page_of_reserved_books = WebElement(xpath='//*[@class="b-header-b-personal-e-icon '
                                              'b-header-b-personal-e-icon-m-putorder b-header-e-sprite-background"]')
    # Кнопка корзины
    cart = WebElement(xpath='//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-cart  '
                            'b-header-e-sprite-background"]')
    book_1 = WebElement(xpath='//span[@class="product-title large-name"]''[1]')
    # Чекбокс на странице корзины
    buy_checkbox = WebElement(xpath='//*[@id="basket-step1-default"]/div[2]/div[2]/div/div/div[1]/div/div[6]/label'
                                    '/span')
    cookie = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/button')
    # Удаление на странице корзины
    remove = WebElement(xpath='//*[@id="step1-default"]/div/div/a[4]')
    message_remove = WebElement(xpath='//span[Compare(test(), "Ваша корзина пуста. Почему?") and '
                                      '@class="b-link-popup"ey g-alttext-head"]')
    order = WebElement(xpath='//input[@class="btn btn-small btn-more"]')
    message_order = WebElement(xpath='//span[Compare(text(), "КУДА ДОСТАВИТЬ ") and @class="g-alttext-small '
                                     'g-alttext-grey g-alttext-head"]')
    order_1 = WebElement(xpath='//button[@class="btn btn-primary btn-large fright start-checkout-js"]')

    # Кнопка "Доставка и оплата"
    shipping_and_payment = WebElement(xpath='//a[@href="/help/"]')
    # Кнопка "Сертификаты"
    certificates = WebElement(xpath='//a[@href="/top/certificates/"]')
    # Кнопка "Рейтинги"
    ratings = WebElement(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')
    # Кнопка "Новинки"
    novelty = WebElement(xpath='//a[@href="/novelty/"]')
    # Кнопка "Скидки"
    discounts = WebElement(xpath='//a[@href="/sale/"]')
    # Кнопка "Контакты"
    contact = WebElement(xpath='//*[@data-event-content="Контакты"]')
    # Кнопка "Поддержка"
    support = WebElement(xpath='//a[@href="/support/"]')
    # Кнопка "Пункты самовывоза"
    pick_up_points = WebElement(xpath='//a[@href="/maps/"]')
    # Кнопка "Регион доставки"
    region = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[12]/span[1]/'
                              'span/span[3]/span')
    field_region = WebElement(xpath='//*[@id="region-post"]')
    region_click = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]')
    message_region = WebElement(xpath='//span[@title="Санкт-Петербург"]')

    # Кнопка "Вконтакте" в footer
    social_vk_f = WebElement(xpath='//a[@data-event-content="ВКонтакте"]')
    # Кнопка "Вконтакте. Дети" в footer
    social_vk_child_f = WebElement(xpath='//a[@data-event-content="ВКонтакте. Дети"]')
    # Кнопка "Ютьюб" в footer
    social_youtube_f = WebElement(xpath='//a[@data-event-content="Ютьюб"]')
    # Кнопка "Инстаграм" в footer
    social_instagram_f = WebElement(xpath='//a[@data-event-content="Инстаграм"]')
    # Кнопка "Инстаграм. Дети" в footer
    social_instagram_child_f = WebElement(xpath='//a[@data-event-content="Инстаграм. Дети"]')
    # Кнопка "Фейсбук" в footer
    social_facebook_f = WebElement(xpath='//a[@data-event-content="Фейсбук"]')
    # Кнопка "Одноклассники" в footer
    social_ok_f = WebElement(xpath='//a[@data-event-content="Одноклассники"]')
    # Кнопка "Твиттер" в footer
    social_twitter_f = WebElement(xpath='//a[@data-event-content="Твиттер"]')
    # Кнопка "Дзен" в footer
    social_zen_f = WebElement(xpath='//a[@data-event-content="Дзен"]')
    # Кнопка "Телеграм" в footer
    social_telegram_f = WebElement(xpath='//a[@data-event-content="Телеграм"]')
    # Кнопка "ТикТок" в footer
    social_tiktok_f = WebElement(xpath='//a[@data-event-content="ТикТок"]')
    message_tiktok = WebElement(xpath='//span[Compare(test()), "labirintru") and @class="profile"]')

    # Кнопка "В Корзину" на главной странице
    buy = WebElement(xpath='//*[@class="btn buy-link btn-primary"]')
    message_buy = WebElement(xpath='//span[Compare(test()), "1") and @class="b-header-b-personal-e-icon-count-m-cart '
                                   'basket-in-cart-a"]')
    # Кнопка "Добавить в отложенные" на главной странице
    reserved_books = WebElement(xpath='//a[@class="icon-fave"]')
    message_reserved_book = WebElement(xpath='//span[Compare(test()), "1") and '
                                             '@class="b-header-b-personal-e-icon-count-m-putorder '
                                             'basket-in-dreambox-a"]')
    # Кнопка "Еще действия" на главной странице
    more = WebElement(xpath='//*[@data-tooltip_title="Еще действия"]''[1]')
    # Кнопка "Добавить к сравнению" на главной странице
    compare = WebElement(xpath='//*[@class="b-list-item-hover js-card-block-actions-compare"]')
    message_compare = WebElement(xpath='//span[Compare(test()), "1") and @class="cabinet-menu__counter"]')
    # Книга на главной странице
    book = WebElement(xpath='//*[@class="card-column card-column_gutter-60 swiper-slide swiper-slide-active"]')
    message_book = WebElement(xpath='//*[@class="prodtitle"]')
    # Кнопка "Больше книг со скидками"
    more_books_with_discounts = WebElement(xpath='//*[@class="btn btn-not-avaliable autodiscounts__btn '
                                                 'autodiscounts__padding"]')

    # Кнопка "В Корзину" на странице книги
    buy_book_page = WebElement(xpath='//*[@class="btn btn-small btn-primary btn-buy"]')
    message_buy_book_page = WebElement(xpath='//span[Compare(test()), "1") and '
                                             '@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')
    # Кнопка "Добавить в отложенные" на странице книги
    reserved_books_book_page = WebElement(xpath='//a[@class="fave"]')
    message_reserved_book_book_page = WebElement(xpath='//span[Compare(test()), "1") and '
                                                       '@class="b-header-b-personal-e-icon-count-m-putorder '
                                                       'basket-in-dreambox-a"]')
    # Кнопка "Добавить к сравнению" на странице книги
    compare_book_page = WebElement(xpath='//*[@class="compare big-compare"]')
    # Кнопка "Сравнить" на странице книги
    compare_book = WebElement(xpath='//*[@class="compare big-compare done"]')
    message_compare_book_page = WebElement(xpath='//span[Compare(test()), "1") and @class="cabinet-menu__counter"]')

    # Страница результатов поиска

    # Названия книг, полученных в результате поиска
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/books/") and @title!=""]')
    # Цены книг, полученных в результате поиска
    products_prices = ManyWebElements(xpath='//span[@class="price-val"]//span')

    # Кнопка фильтра по типу товара
    sort_products_by_type = WebElement(xpath='//*[@id="catalog-navigation"]/form[1]/div[1]/div[1]/div[1]/div[1]'
                                             '/span[1]/span[1]/span[1]/span[1]')
    # Кнопка фильтра по типу товара (Бумажные книги)
    paper_books = WebElement(xpath='//*[@id="catalog-navigation"]/form[1]/div[1]/div[1]/div[1]/div[1]'
                                   '/span[1]/span[1]/span[1]/span[2]/ul[1]/li[1]/label[1]')
    # Кнопка фильтра по типу товара (Другие товары)
    other_books = WebElement(xpath='//*[@id="catalog-navigation"]/form[1]/div[1]/div[1]/div[1]/div[1]'
                                   '/span[1]/span[1]/span[1]/span[2]/ul[1]/li[2]/label[1]')
    # Кнопка фильтра по типу товара (Показать)
    button_show_type = WebElement(xpath='//input[@class="w100p show-goods__button"]')

    # Кнопка фильтра наличия
    sort_products_by_availability = WebElement(xpath='//span[@class="navisort-part navisort-filter navisort-part-2 '
                                                     'fleft"]')
    # Кнопка фильтра наличия (В наличии)
    available = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[2]/span/span/span[2]'
                                 '/ul/li[1]')
    # Кнопка фильтра наличия (Предзаказ)
    preorder = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[2]/span/span/span[2]'
                                '/ul/li[2]')
    # Кнопка фильтра наличия (Ожидаются)
    wait = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[2]/span/span/span[2]'
                            '/ul/li[3]')
    # Кнопка фильтра наличия (Нет в продаже)
    no = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[2]/span/span/span[2]'
                          '/ul/li[4]')
    # Кнопка фильтра наличия (Показать)
    button_show_availability = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[2]'
                                                '/span/span/span[2]/ul/li[6]')

    # Кнопка фильтра цены
    sort_products_by_price = WebElement(xpath='//span[contains(text(), "ЦЕНА") and @class="navisort-item__content"]')
    # Кнопка фильтра цены (Со скидкой)
    with_discounts = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span'
                                      '/span[2]/ul/li[2]/label')
    # Кнопка фильтра цены (С кэшбэком)
    with_cashback = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span'
                                     '/span[2]/ul/li[3]/label')
    # Кнопка фильтра цены (Курьером бесплатно)
    free_delivery = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span/span'
                                     '/span[2]/ul/li[4]/label')
    check = WebElement(xpath='//img[@class="book-img-cover"]')
    # Кнопка фильтра цены (Показать)
    button_show_price = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[3]/span'
                                         '/span/span[2]/ul/li[6]/input')

    # Кнопка всех фильтров
    all_filters = WebElement(xpath='//*[@id="catalog-navigation"]/form/div[1]/div[1]/div/div/span[5]/span'
                                   '/span/span/span')
    # Кнопка всех фильтров (Тип товара/ Прочие товары)
    all_type_another = WebElement(xpath='//*[@id="section-search-form"]/div[1]/div[2]/div[2]/label/span[1]')
    # Кнопка всех фильтров (Наличие/ Предзаказ)
    all_available_preorder = WebElement(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[2]')
    # Кнопка всех фильтров (Наличие/ Ожидаются)
    all_available_wait = WebElement(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[3]')
    # Кнопка всех фильтров (Наличие/ Нет в продаже)
    all_available_no = WebElement(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[4]')

    # Кнопка всех фильтров (Цена)
    all_price = WebElement(xpath='//*[@id="section-search-form"]/div[3]')
    # Кнопка всех фильтров (Цена/ Со скидкой)
    all_price_with_discounts = WebElement(xpath='//*[@id="section-search-form"]/div[3]/div[2]/div[3]')

    # Кнопка всех фильтров (Для кого)
    all_for_whom = WebElement(xpath='//*[@id="section-search-form"]/div[4]')
    # Кнопка всех фильтров (Для кого/ Только взрослым)
    all_for_whom_adult_only = WebElement(xpath='//*[@id="section-search-form"]/div[4]/div[2]/div[1]')

    # Кнопка всех фильтров (Описание)
    all_description = WebElement(xpath='//*[@id="section-search-form"]/div[5]')
    # Кнопка всех фильтров (Описание/ С фото)
    all_description_with_photo = WebElement(xpath='//*[@id="section-search-form"]/div[5]/div[2]/div[2]')

    # Кнопка всех фильтров (Сбросить)
    all_reset = WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[1]/div[1]/div[2]/div[1]/span[3]')
    # Кнопка всех фильтров (Показать)
    all_show = WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[1]/div[1]/div[2]/input[1]')
    result_all_filter = WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/div/div[2]/div/div[1]/a')
    result_all_filter_1 = WebElement(xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/div/div[1]/div/div[1]/a')
    message_all = WebElement(xpath='//div[@title=" Цена с учетом скидки по акции "Читаем дома" (22%)"]')
    message_all_1 = WebElement(xpath='//img[@src="https://img4.labirint.ru/rc/3fcdbb058ed513c9446a339f60255606/220x340'
                                     '/books76/752678/cover.jpg?1593365225"]')
    message_all_2 = WebElement(xpath='//div[contains(text(), "16+") and @title="Рекомендуемый возраст"]')
    message_all_3 = WebElement(xpath='//span[contains(text(), "Добавить ") and @class="text"]')
    message_all_book = WebElement(xpath='//div[@class="prodtitle"]')
