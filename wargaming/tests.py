def test_weapon1(db_created):
    s, m = db_created
    test_input = 'ship_1'
    w0 = s.executemany("SELECT weapon FROM Ships where ship = ?;", test_input)
    w1 = m.executemany("SELECT weapon FROM Ships where ship = ?;", test_input)
    assert w0 == w1
# Ах, как же все хорошо начиналось...
# Надеюсь что не забуду про это тестовое и вернусь к нему позже...
