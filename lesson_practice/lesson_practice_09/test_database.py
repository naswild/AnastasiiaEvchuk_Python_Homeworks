from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"

def test_db_connection():
    engine = create_engine(db_connection_string)
    inspector = inspect(engine)
    names = inspector.get_table_names()
    assert names[1] == "company"
    print(names)

def test_select():
    engine = create_engine(db_connection_string)
    connection = engine.connect()
    result = connection.execute(text("select * from company"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1.get("id") == 1
    assert row1.get("name") == "QA Студия 'ТестировщикЪ'"
    print(row1.get("name"))

    connection.close()

def test_select_1_row():
    engine = create_engine(db_connection_string)
    connection = engine.connect()
    sql_statement = text("select * from company where id = :company_id")
    result = connection.execute(sql_statement, {"company_id":2})
    rows = result.mappings().all()

    assert len(rows) == 1
    assert rows[0].get("name") == "Автоматизация тестирования"

    connection.close()

def test_select_1_row_with_two_filters():
    engine = create_engine(db_connection_string)
    connection = engine.connect()
    sql_statement = text("select * from company where id >= :company_id and is_active = :is_active")
    result = connection.execute(sql_statement, {"company_id":4, "is_active":True})
    rows = result.mappings().all()
    assert len(rows) == 3
    assert rows[0].get("name") == "Консалтинговая компания 'QA-Эксперт'"
    connection.close()

def test_insert():
    engine = create_engine(db_connection_string)
    connection = engine.connect()
    transaction = connection.begin()
    sql_statement = text("insert into company (name) values (:new_name)")
    connection.execute(sql_statement, {"new_name": "Skypro"})

    transaction.commit()
    connection.close()

def test_update():
    engine = create_engine(db_connection_string)
    connection = engine.connect()
    transaction = connection.begin()
    sql_statement = text("update company set description = :description where id = :company_id")
    connection.execute(sql_statement, {"description":"New description", "company_id": 12})

    transaction.commit()
    connection.close()

def test_delete():
    engine = create_engine(db_connection_string)
    connection = engine.connect()
    transaction = connection.begin()

    sql_statement = text("delete from company where id = :company_id")
    connection.execute(sql_statement, {"company_id": 12})

    transaction.commit()
    connection.close()