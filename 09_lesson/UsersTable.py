from sqlalchemy import create_engine, text


class UsersTable:

    __scripts = {
        "insert_new": text("insert into users (user_id, user_email, subject_id) values (:user_id, :user_email, :subject_id)"),
    }
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def add_user(self, user_id, user_email, subject_id):
        connection = self.db.connect()
        connection.execute(self.__scripts["insert_new", {"user_id": user_id, "user_email": user_email, "subject_id": subject_id}])
        connection.commit()
        connection.close()
