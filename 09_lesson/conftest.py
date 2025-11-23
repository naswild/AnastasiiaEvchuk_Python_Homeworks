import pytest
from sqlalchemy import create_engine

from StudentTable import StudentTable
from TeacherTable import TeacherTable
from UsersTable import UsersTable


@pytest.fixture
def db_connection_flow():
    db = create_engine("postgresql://user:pw@localhost:5432/mydb")
    connection = db.connect()
    yield connection
    connection.commit()
    connection.close()

@pytest.fixture
def users(db_connection_flow):
    return UsersTable(db_connection_flow)


@pytest.fixture
def student(db_connection_flow):
    return StudentTable(db_connection_flow)


@pytest.fixture
def teacher(db_connection_flow):
    return TeacherTable(db_connection_flow)