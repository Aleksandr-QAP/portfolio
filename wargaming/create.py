import sqlite3
import random

conn = sqlite3.connect(r'SQLite/main.db')  # Создаем DB

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Ships(
    ship TEXT PRIMARY KEY,
    weapon TEXT REFERENCES Weapons(weapon),
    hull TEXT REFERENCES Hulls(hull),
    engine TEXT REFERENCES Engines(engine)
    );
""")  # Создаем таблицу Ships
conn.commit()  # Сохраняем изменения

i = 1
while i <= 200:  # Задаем количество заполняемых строк
    name_ships = 'ship_' + str(i)  # Определяем заполнение колонки 'ship'
    name_weapons = 'weapon_' + str(i)  # Определяем заполнение колонки 'weapon'
    name_hulls = 'hull_' + str(i)  # Определяем заполнение колонки 'hull'
    name_engines = 'engine_' + str(i)  # Определяем заполнение колонки 'ship'
    more_ships = [(name_ships, name_weapons, name_hulls, name_engines)]  # Формируем кортеж
    cur.executemany("INSERT INTO Ships VALUES(?, ?, ?, ?);", more_ships)  # Заполняем таблицу данными
    i += 1

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Weapons(
    weapon TEXT PRIMARY KEY,
    reload_speed INT,
    rotation_speed INT,
    diameter INT,
    power_volley INT,
    count INT);
""")  # Создаем таблицу Weapons
conn.commit()

i = 1
while i <= 20:
    name_weapons = 'weapon_' + str(i)
    more_weapons = [(name_weapons, random.randint(1, 20), random.randint(1, 20),
                     random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))]
    cur.executemany("INSERT INTO Weapons VALUES(?, ?, ?, ?, ?, ?);", more_weapons)
    i += 1

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Hulls(
    hull TEXT PRIMARY KEY,
    armor INT,
    type INT,
    capacity INT);
""")  # Создаем таблицу Hulls
conn.commit()

i = 1
while i <= 5:
    name_hulls = 'hull_' + str(i)
    more_hulls = [(name_hulls, random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))]
    cur.executemany("INSERT INTO Hulls VALUES(?, ?, ?, ?);", more_hulls)
    i += 1

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Engines(
    engine TEXT PRIMARY KEY,
    power INT,
    type INT);
""")  # Создаем таблицу Engines

conn.commit()

i = 1
while i <= 6:
    name_engines = 'engine_' + str(i)
    more_engines = [(name_engines, random.randint(1, 20), random.randint(1, 20))]
    cur.executemany("INSERT INTO Engines VALUES(?, ?, ?);", more_engines)
    i += 1

conn.commit()
