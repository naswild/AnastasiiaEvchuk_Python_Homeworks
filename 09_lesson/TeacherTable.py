from sqlalchemy import text


class TeacherTable:

    __scripts = {
        "create_teacher": text("insert into teacher (teacher_id, email, group_id) "
                               "values (:teacher_id, :email, :group_id)"),
        "select_by_id": text("select * from teacher where teacher_id = :teacher_id"),
        "delete_by_id": text("delete from teacher where teacher_id = :teacher_id"),
        "select_count": text("select count(*) from teacher")
    }

    def __init__(self, connection):
        self.connection = connection

    def create_teacher(self, teacher_id, email, group_id):
        self.connection.execute(self.__scripts["create_teacher"], {"teacher_id": teacher_id,
                                                              "email": email,
                                                              "group_id": group_id})

    def delete_teacher_by_id(self, teacher_id):
        self.connection.execute(self.__scripts["delete_by_id"], {"teacher_id": teacher_id})

    def get_teacher_by_id(self, teacher_id):
        result = self.connection.execute(self.__scripts["select_by_id"], {"teacher_id": teacher_id})
        return result.mappings().all()[0]

    def get_teacher_count(self):
        return self.connection.execute(self.__scripts["select_count"]).scalar()
