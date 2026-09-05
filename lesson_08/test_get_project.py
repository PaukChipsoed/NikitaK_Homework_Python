from project_api import ProjectApi


def test_get_project(api_headers, create_project):
    api = ProjectApi(api_headers)

    response = api.get_project(create_project)

    assert response.status_code == 200
    assert response.json()["id"] == create_project


def test_get_project_with_invalid_id(api_headers):
    api = ProjectApi(api_headers)

    invalid_id = "00000000-0000-0000-0000-000000000000"

    response = api.get_project(invalid_id)

    assert response.status_code == 404
