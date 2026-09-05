import uuid

from project_api import ProjectApi


def test_update_project(api_headers, create_project):
    api = ProjectApi(api_headers)

    new_title = f"Updated project {uuid.uuid4()}"

    response = api.update_project(
        create_project,
        new_title,
    )

    assert response.status_code == 200

    get_response = api.get_project(create_project)

    assert get_response.status_code == 200
    assert get_response.json()["title"] == new_title


def test_update_project_with_invalid_id(api_headers):
    api = ProjectApi(api_headers)

    invalid_id = "00000000-0000-0000-0000-000000000000"

    response = api.update_project(
        invalid_id,
        "Updated project",
    )

    assert response.status_code == 404
