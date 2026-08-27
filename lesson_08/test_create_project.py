import uuid

from project_api import ProjectApi


def test_create_project(api_headers):
    api = ProjectApi(api_headers)

    title = f"Test project {uuid.uuid4()}"

    response = api.create_project(title)

    assert response.status_code == 201
    assert response.json()["id"]


def test_create_project_without_title(api_headers):
    api = ProjectApi(api_headers)

    response = api.create_project("")

    assert response.status_code == 400
