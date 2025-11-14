import requests


class ProjectsApi:
    PROJECTS_BASE_ENDPOINT = "/api-v2/projects"

    def __init__(self, url):
        self.url = url

    def create_project(self, title, token):
        project_information = {
            "title": title,
        }

        my_headers = {
            "Authorization": "Bearer " + token
        }

        resp = requests.post(self.url + self.PROJECTS_BASE_ENDPOINT, headers=my_headers, json=project_information)
        return resp

    def get_project_id(self, project):
        return project.json()["id"]

    def get_project_information(self, project_id, token):
        my_headers = {
            "Authorization": "Bearer " + token
        }

        resp = requests.get(self.url + self.PROJECTS_BASE_ENDPOINT + "/" + project_id, headers=my_headers)
        return resp

    def change_project_title(self, token, new_title, project_id):
        new_title = {
            "title": new_title
        }

        my_headers = {
            "Authorization": "Bearer " + token
        }

        resp = requests.put(self.url + self.PROJECTS_BASE_ENDPOINT + "/" + project_id, headers=my_headers, json=new_title)
        return resp
