from CompanyApi import CompanyApi
from lesson_practice_09.CompanyTable import CompanyTable

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

def test_get_companies():
    api_result = api.get_company_list()
    db_result = db.get_companies()
    assert len(api_result) == len(db_result)

def test_get_active_companies():
    params_to_add = {
        "active": "true"
    }

    api_result = api.get_company_list(params_to_add)
    db_result = db.get_active_companies()
    assert len(api_result) == len(db_result)


def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    description = "Test company"
    result = api.create_company(name, True, description)
    new_id = result.get("id")

    body = api.get_company_list()
    len_after = len(body)

    db.delete_company(new_id)
    assert len_after - len_before == 1
    for company in body:
        if company.get("id") == new_id:
            assert company.get("name") == name
            assert company.get("description") == description
            assert company.get("active") == "true"

def test_get_one_company():
    name = "Skypro"
    description = "Test company"
    db.create_company(name, description)
    max_id = db.get_max_id()

    new_company = api.get_company(max_id)

    db.delete_company(max_id)