import sqlite3
import random


"""Замена случайного параметра в таблице Weapons"""
i = 1
while i <= 20:
    name_weapon = 'weapon_' + str(i)
    cul = ['reload_speed', 'rotation_speed', 'diameter', 'power_volley', 'count']
    conn = sqlite3.connect(r'SQLite/main.db')
    cur = conn.cursor()
    sql = "Update Weapons set {cul_name} = ? where weapon = ?"
    params = (random.randint(1, 20), name_weapon)
    cur.execute(sql.format(cul_name=random.choice(cul)), params)
    conn.commit()
    i += 1

"""Замена случайного параметра в таблице Hulls"""
i = 1
while i <= 5:
    name_hull = 'hull_' + str(i)
    cul = ['armor', 'type', 'capacity']
    conn = sqlite3.connect(r'SQLite/main.db')
    cur = conn.cursor()
    sql = "Update Hulls set {cul_name} = ? where hull = ?"
    params = (random.randint(1, 20), name_hull)
    cur.execute(sql.format(cul_name=random.choice(cul)), params)
    conn.commit()
    i += 1

"""Замена случайного параметра в таблице Engines"""
i = 1
while i <= 6:
    name_engine = 'engine_' + str(i)
    cul = ['power', 'type']
    conn = sqlite3.connect(r'SQLite/main.db')
    cur = conn.cursor()
    sql = "Update Engines set {cul_name} = ? where engine = ?"
    params = (random.randint(1, 20), name_engine)
    cur.execute(sql.format(cul_name=random.choice(cul)), params)
    conn.commit()
    i += 1

"""Замена компонента в таблице Ships"""
i = 1
while i <= 200:
    name_ship = 'ship_' + str(i)
    cul = ['weapon', 'hull', 'engine']
    conn = sqlite3.connect(r'SQLite/main.db')
    cur = conn.cursor()
    model = random.choice(cul)
    model_i = model + '_' + str(random.randint(1, 200))
    params = (model_i, name_ship)
    sql = "Update Ships set {cul_name} = ? where ship = ?"
    cur.execute(sql.format(cul_name=model), params)
    conn.commit()
    i += 1
