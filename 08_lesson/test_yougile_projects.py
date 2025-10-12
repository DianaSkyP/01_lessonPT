import uuid


class TestYougileProjects:

    def test_create_project_positive(self, api_client, test_project_data):
        response = api_client.create_project(test_project_data)

        assert api_client.is_successful_response(response, [201]), (
            f"Expected 201, got {response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

        response_data = response.json()
        assert "id" in response_data, "Response should contain project ID"
        assert response_data["title"] == test_project_data["title"]
        assert response_data["description"] == test_project_data["description"]

        project_id = response_data["id"]
        cleanup_response = api_client.delete_project(project_id)
        assert cleanup_response.status_code in [200, 204, 404]

    def test_get_project_positive(self, created_project, api_client):
        project_id = created_project["id"]
        original_data = created_project["original_request"]

        response = api_client.get_project(project_id)

        assert api_client.is_successful_response(response, [200]), (
            f"Expected 200, got {response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

        response_data = response.json()
        assert response_data["id"] == project_id
        assert response_data["title"] == original_data["title"]
        assert response_data["description"] == original_data["description"]

    def test_update_project_positive(self, created_project, api_client):
        project_id = created_project["id"]
        original_data = created_project["original_request"]
        updated_data = {
            "title": f"Updated {original_data['title']}",
            "description": "Updated description by automated tests"
        }
        response = api_client.update_project(project_id, updated_data)

        assert api_client.is_successful_response(response, [200]), (
            f"Expected 200, got {response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

        response_data = response.json()
        assert response_data["title"] == updated_data["title"]
        assert response_data["description"] == updated_data["description"]

    def test_create_multiple_projects(self, api_client, project_cleanup_list):
        projects_to_create = [
            {
                "title": f"Batch Project 1 {uuid.uuid4().hex[:6]}",
                "description": "First batch project"
            },
            {
                "title": f"Batch Project 2 {uuid.uuid4().hex[:6]}",
                "description": "Second batch project"
            },
        ]

        created_ids = []

        for project_data in projects_to_create:

            project_id = api_client.create_project_and_get_id(project_data)
            created_ids.append(project_id)
            project_cleanup_list.append(project_id)
        assert len(created_ids) == 2

        for project_id in created_ids:
            assert api_client.project_exists(project_id), (
                f"Project {project_id} should exist"
            )

    def test_create_project_negative_empty_title(self, api_client):
        invalid_data = {
            "description": "Project without title",
            "users": []
        }
        response = api_client.create_project(invalid_data)

        assert api_client.is_successful_response(response, [400, 422]), (
            f"Expected 400 or 422 for missing title, got "
            f"{response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

    def test_create_project_negative_invalid_data(self, api_client):
        invalid_data = {
            "title": "",
            "description": None,
            "users": "invalid"
        }
        response = api_client.create_project(invalid_data)

        assert api_client.is_successful_response(response, [400, 422]), (
            f"Expected 400 or 422 for invalid data, got "
            f"{response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

    def test_get_project_negative_nonexistent_id(self, api_client):
        nonexistent_id = "nonexistent-project-id-12345"
        assert not api_client.project_exists(nonexistent_id), (
            "Test project should not exist before test"
        )

        response = api_client.get_project(nonexistent_id)

        assert api_client.is_successful_response(response, [404]), (
            f"Expected 404 for nonexistent project, got "
            f"{response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

    def test_get_project_negative_invalid_id_format(self, api_client):
        invalid_id = "invalid-id-format-!@#$%"
        try:
            response = api_client.get_project(invalid_id)
            assert api_client.is_successful_response(response, [400, 404]), (
                f"Expected 400 or 404 for invalid ID format, got "
                f"{response.status_code}. "
                f"Error: {api_client.get_error_message(response)}"
            )
        except ValueError as e:

            assert "Project ID must be a non-empty string" in str(e)

    def test_update_project_negative_nonexistent_id(self, api_client):
        nonexistent_id = "nonexistent-project-id-12345"
        update_data = {"title": "Updated title"}
        assert not api_client.project_exists(nonexistent_id)

        response = api_client.update_project(nonexistent_id, update_data)

        assert api_client.is_successful_response(response, [404]), (
            f"Expected 404 for nonexistent project, got "
            f"{response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

    def test_update_project_negative_invalid_data(self, created_project,
                                                  api_client):
        project_id = created_project["id"]
        invalid_update_data = {
            "title": None,
            "description": 12345
        }

        response = api_client.update_project(project_id, invalid_update_data)

        assert api_client.is_successful_response(response, [400, 422]), (
            f"Expected 400 or 422 for invalid update data, got "
            f"{response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

    def test_delete_project_negative_nonexistent_id(self, api_client):
        nonexistent_id = "nonexistent-project-id-12345"
        assert not api_client.project_exists(nonexistent_id)

        response = api_client.delete_project(nonexistent_id)
        assert api_client.is_successful_response(response, [200, 204, 404]), (

            f"Expected 200, 204 or 404 for nonexistent project deletion, "
            f"got {response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )
