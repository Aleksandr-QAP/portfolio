Вступление
------------
Данный репозиторий содержит парсер автомобилей для https://auto.ria.com/ и парсер статей для https://stopgame.ru/.
По окончанию парсинга вся информация сохраняется в cars.csv (https://auto.ria.com/) и title.csv (https://stopgame.ru/).

Файлы
-----

[auto_ria.py](auto_ria.py) содержит необходимый код для парсинга автомобилей https://auto.ria.com/.

[stopgame.py](stopgame.py) содержит необходимый код для парсинга статей https://stopgame.ru/


Запуск Скрипта
----------------

1) Установить все зависимости:


    pip3 install -r requirements.txt


2)Запуск скрипта:

    python auto_ria.py

или

    python stopgame.py

PS
----------------

После запуска от пользователя потребуется ввод URL страницы.
Для [auto_ria.py](auto_ria.py) возможно задать ссылки для поддержаных и новых автомобилей.
Для [stopgame.py](stopgame.py) возможно задать ссылки сраниц с обзорами.