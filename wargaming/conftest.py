import sqlite3
import random
import pytest


@pytest.fixture(scope="session")
def db_created():
    source = sqlite3.connect(r'SQLite/main.db')
    s = source.cursor()
    print("Connection is established: Database from HDD activate")
    mem = sqlite3.connect(':memory:')
    m = mem.cursor()
    print("Connection is established: Database is created in memory")
    source.backup(mem)
    source.commit()

    i = 1
    while i <= 20:
        name_weapon = 'weapon_' + str(i)
        cul = ['reload_speed', 'rotation_speed', 'diameter', 'power_volley', 'count']
        sql = "Update Weapons set {cul_name} = ? where weapon = ?"
        params = (random.randint(1, 20), name_weapon)
        m.execute(sql.format(cul_name=random.choice(cul)), params)
        i += 1
        mem.commit()

    i = 1
    while i <= 5:
        name_hull = 'hull_' + str(i)
        cul = ['armor', 'type', 'capacity']
        sql = "Update Hulls set {cul_name} = ? where hull = ?"
        params = (random.randint(1, 20), name_hull)
        m.execute(sql.format(cul_name=random.choice(cul)), params)
        mem.commit()
        i += 1

    i = 1
    while i <= 6:
        name_engine = 'engine_' + str(i)
        cul = ['power', 'type']
        sql = "Update Engines set {cul_name} = ? where engine = ?"
        params = (random.randint(1, 20), name_engine)
        m.execute(sql.format(cul_name=random.choice(cul)), params)
        mem.commit()
        i += 1

    i = 1
    while i <= 200:
        name_ship = 'ship_' + str(i)
        cul = ['weapon', 'hull', 'engine']
        model = random.choice(cul)
        model_i = model + '_' + str(random.randint(1, 200))
        params = (model_i, name_ship)
        sql = "Update Ships set {cul_name} = ? where ship = ?"
        m.execute(sql.format(cul_name=model), params)
        i += 1
        mem.commit()

    return s, m

