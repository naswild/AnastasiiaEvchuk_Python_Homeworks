import requests


class AuthorizationApi:
    GET_COMPANY_ENDPOINT = "/api-v2/auth/companies"
    CREATE_KEY_ENDPOINT = "/api-v2/auth/keys"
    GET_KEYS_ENDPOINT = "/api-v2/auth/keys/get"

    def __init__(self, url):
        self.url = url

    def get_company_id(self, login, password):
        credentials = {
            "login": login,
            "password": password
        }
        resp = requests.post(self.url + self.GET_COMPANY_ENDPOINT, json=credentials)
        return resp.json().get("content", [{}])[0].get("id")

    def get_key(self, login, password):
        company_id = self.get_company_id(login, password)
        credentials = {
            "login": login,
            "password": password,
            "companyId": company_id
        }
        resp = requests.post(self.url + self.GET_KEYS_ENDPOINT, json=credentials)
        if resp.json()[0] is not None:
            return (resp.json()[0] or [{}]).get("key")
        resp = requests.post(self.url + self.CREATE_KEY_ENDPOINT, json=credentials)
        return resp.json()["key"]
