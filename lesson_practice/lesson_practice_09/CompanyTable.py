from sqlalchemy import create_engine, inspect, text


class CompanyTable:

    __scripts = {
        "select": text("select * from company where deleted_at IS NULL"),
        "select_active": text("select * from company where is_active = true and deleted_at IS NULL"),
        "delete_by_id": text("delete from company where id = :id_to_delete"),
        "insert_new": text("insert into company (name, description) values (:new_name, :description)"),
        "get_max_id": text("select max(id) from company where deleted_at IS NULL"),

    }
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_companies(self):
        connection = self.db.connect()
        result = connection.execute(self.__scripts["select"])
        rows = result.mappings().all()
        connection.close()
        return rows

    def get_active_companies(self):
        connection = self.db.connect()
        result = connection.execute(self.__scripts["select_active"])
        rows = result.mappings().all()
        connection.close()
        return rows

    def delete_company(self, id):
        connection = self.db.connect()
        connection.execute(self.__scripts["delete_by_id"], {"id_to_delete": id})
        connection.commit()
        connection.close()

    def create_company(self, new_name, description):
        connection = self.db.connect()
        connection.execute(self.__scripts["insert_new"], {"new_name": new_name, "description": description})
        connection.commit()
        connection.close()

    def get_max_id(self):
        connection = self.db.connect()
        max_id = connection.execute(self.__scripts["get_max_id"]).scalar()
        connection.close()
        return max_id