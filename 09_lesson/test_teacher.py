import pytest

@pytest.mark.db_teacher_positive_test
def test_delete_teacher(teacher):
    teacher_id = 75932
    email = "teacher_spanish@gato.com"
    group_id = 28
    teacher.create_teacher(teacher_id, email, group_id)
    count_before = teacher.get_teacher_count()
    teacher.delete_teacher_by_id(teacher_id)
    count_after = teacher.get_teacher_count()
    assert count_before - count_after == 1
