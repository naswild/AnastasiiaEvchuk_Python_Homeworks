from sqlalchemy import text


class UsersTable:

    __scripts = {
        "insert_new": text("insert into users (user_id, user_email, subject_id) values (:user_id, :user_email, :subject_id)"),
        "select_by_id": text("select * from users where user_id = :user_id"),
        "delete_by_id": text("delete from users where user_id = :id_to_delete"),
        "select_count": text("select count(*) from users")
    }

    def __init__(self, connection):
        self.connection = connection

    def add_user(self, user_id, user_email, subject_id):
        self.connection.execute(self.__scripts["insert_new"], {"user_id": user_id,
                                                         "user_email": user_email,
                                                         "subject_id": subject_id})

    def get_user_by_id(self, user_id):
        result = self.connection.execute(self.__scripts["select_by_id"], {"user_id": user_id})
        return result.mappings().all()[0]

    def delete_user_by_id(self, user_id):
        self.connection.execute(self.__scripts["delete_by_id"], {"id_to_delete": user_id})

    def get_users_count(self):
        return self.connection.execute(self.__scripts["select_count"]).scalar()