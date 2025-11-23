import pytest


@pytest.mark.db_users_positive_test
def test_add_user(users):
    user_id = 2858
    count_before = users.get_users_count()
    users.add_user(user_id, "kgds@jkj.com", "4")
    count_after = users.get_users_count()
    assert users.get_user_by_id(user_id).get("user_id") == user_id
    assert count_after - count_before == 1
    users.delete_user_by_id(user_id)
