from UsersTable import UsersTable

users = UsersTable("")

def test_add_user(user_id, user_email, subject_id):
    users.add_user(user_id, user_email, subject_id)
