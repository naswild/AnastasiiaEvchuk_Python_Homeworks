import pytest


@pytest.mark.db_student_positive_test
def test_change_level(student):
    user_id = 237483
    level = "Pre-Intermediate"
    education_form = "personal"
    subject_id = 8
    new_level = "Advanced"
    student.create_student(user_id, level, education_form, subject_id)
    student.change_level_by_id(user_id, new_level)
    assert student.get_student_by_id(user_id).get("level") == new_level
    student.delete_student_by_id(user_id)

