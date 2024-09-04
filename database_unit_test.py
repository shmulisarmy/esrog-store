from esrogimDb import EsrogimDB




test_db = EsrogimDB("test.db")





def test_create_table():
    test_db.create_table()
    table_info = test_db.table_info()
    assert table_info["id"] == "INTEGER"
    assert table_info["size"] == "INTEGER"
    assert table_info["clenleaness"] == "INTEGER"
    assert table_info["chabad"] == "INTEGER"
    assert table_info["reservedBy"] == "INTEGER"
    assert table_info["sold"] == "boolean"



def test_insert_esrog():
    row_id = test_db.insert_esrog(2, 3, 4)
    result = test_db.get_esrog_by_id(row_id)
    assert result == (row_id, 2, 3, 4, None)


def test_update_esrog():
    test_db.update_esrog(1, 2, 3, 4)
    result = test_db.get_esrog_by_id(1)
    assert result == (1, 2, 3, 4, None)


print(test_db.table_info())
