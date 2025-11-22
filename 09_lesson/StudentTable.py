from sqlalchemy import text


class StudentTable:

    __scripts = {
        "create_student": text("insert into student (user_id, level, education_form, subject_id) "
                               "values (:user_id, :level, :education_form, :subject_id)"),
        "change_level_by_id": text("update student set level = :new_level where user_id = :user_id"),
        "select_by_id": text("select * from student where user_id = :user_id"),
        "delete_by_id": text("delete from student where user_id = :user_id")
    }

    def __init__(self, connection):
        self.connection = connection

    def create_student(self, user_id, level, education_form, subject_id):
        self.connection.execute(self.__scripts["create_student"], {"user_id": user_id,
                                                              "level": level,
                                                              "education_form": education_form,
                                                              "subject_id": subject_id})

    def change_level_by_id(self, user_id, new_level):
        self.connection.execute(self.__scripts["change_level_by_id"], {"user_id": user_id, "new_level": new_level})

    def get_student_by_id(self, user_id):
        result = self.connection.execute(self.__scripts["select_by_id"], {"user_id": user_id})
        return result.mappings().all()[0]

    def delete_student_by_id(self, user_id):
        self.connection.execute(self.__scripts["delete_by_id"], {"user_id": user_id})
