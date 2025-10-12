import pytest
import uuid
from yougile_api import YougileAPI


@pytest.fixture
def api_client():
    return YougileAPI()


@pytest.fixture
def test_project_data():
    unique_name = f"Test Project {uuid.uuid4().hex[:8]}"
    return {
        "title": unique_name,
        "description": "Test project created by automated tests",
        "users": []
    }


@pytest.fixture
def created_project(api_client, test_project_data):
    response = api_client.create_project(test_project_data)
    assert response.status_code == 201, (
        f"Failed to create project: {response.status_code}"
    )

    project_data = response.json()
    project_id = project_data["id"]

    yield {
        "id": project_id,
        "data": project_data,
        "original_request": test_project_data
    }
    cleanup_response = api_client.delete_project(project_id)
    assert cleanup_response.status_code in [200, 204, 404], (
        f"Failed to cleanup project {project_id}: "
        f"{cleanup_response.status_code}"
    )


@pytest.fixture
def project_cleanup_list(api_client):
    project_ids = []

    yield project_ids

    for project_id in project_ids:
        cleanup_response = api_client.delete_project(project_id)
        assert cleanup_response.status_code in [200, 204, 404], (
            f"Failed to cleanup project {project_id}: "
            f"{cleanup_response.status_code}"
        )
