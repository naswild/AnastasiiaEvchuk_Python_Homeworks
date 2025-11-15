import pytest
import uuid
import os
from dotenv import load_dotenv
from AuthorizationApi import AuthorizationApi
from ProjectsApi import ProjectsApi

BASE_URL = "https://ru.yougile.com"
TITLE = "First test title"
NEW_TITLE = "New title after changing"
authorization = AuthorizationApi(BASE_URL)
projects = ProjectsApi(BASE_URL)

load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

@pytest.mark.yougile_positive_test_create_project
def test_create_project():
    token = authorization.get_key(login, password)
    resp = projects.create_project(TITLE, token)
    project_id = resp.json().get("id")
    assert resp.status_code == 201
    assert project_id is not None
    assert project_id != ""

@pytest.mark.yougile_negative_test_create_project
def test_create_project_with_invalid_token():
    token = str(uuid.uuid4())
    resp = projects.create_project(TITLE, token)

    assert resp.status_code == 401
    assert resp.json().get("statusCode") == 401
    assert resp.json().get("message") == "Unauthorized"
    assert resp.json().get("error") == "Unauthorized"

@pytest.mark.yougile_positive_test_get_project
def test_get_project():
    token = authorization.get_key(login, password)
    project = projects.create_project(TITLE, token)
    project_id = projects.get_project_id(project)
    resp = projects.get_project_information(project_id, token)

    assert resp.status_code == 200
    assert resp.json().get("title") == TITLE
    assert resp.json().get("timestamp") is not None
    assert resp.json().get("id") == project_id

@pytest.mark.yougile_negative_test_get_project
def test_get_project_with_invalid_project_id():
    token = authorization.get_key(login, password)
    project_id = str(uuid.uuid4())
    resp = projects.get_project_information(project_id, token)

    assert resp.status_code == 404
    assert resp.json().get("statusCode") == 404
    assert resp.json().get("message") == "Проект не найден"
    assert resp.json().get("error") == "Not Found"

@pytest.mark.yougile_positive_test_change_project
def test_change_project():
    token = authorization.get_key(login, password)
    project = projects.create_project(TITLE, token)
    project_id = projects.get_project_id(project)
    resp = projects.change_project_title(token, NEW_TITLE, project_id)

    assert resp.status_code == 200
    assert resp.json().get("id") == project_id

@pytest.mark.yougile_negative_test_change_project
def test_change_project_with_invalid_project_id():
    token = authorization.get_key(login, password)
    project_id = str(uuid.uuid4())
    resp = projects.change_project_title(token, NEW_TITLE, project_id)

    assert resp.status_code == 404
    assert resp.json().get("statusCode") == 404
    assert resp.json().get("message") == "Проект не найден"
    assert resp.json().get("error") == "Not Found"
