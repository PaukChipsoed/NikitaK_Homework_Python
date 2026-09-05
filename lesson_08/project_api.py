import requests


BASE_URL = "https://yougile.com/api-v2"


class ProjectApi:

    def __init__(self, headers):
        self.headers = headers

    def create_project(self, title):
        data = {
            "title": title
        }

        return requests.post(
            f"{BASE_URL}/projects",
            headers=self.headers,
            json=data,
        )

    def get_project(self, project_id):
        return requests.get(
            f"{BASE_URL}/projects/{project_id}",
            headers=self.headers,
        )

    def update_project(self, project_id, title):
        data = {
            "title": title
        }

        return requests.put(
            f"{BASE_URL}/projects/{project_id}",
            headers=self.headers,
            json=data,
        )
