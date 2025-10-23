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
        assert isinstance(response_data["id"], str), (
            "Project ID should be string"
        )
        assert response_data["id"], "Project ID should not be empty"

        project_id = response_data["id"]
        cleanup_response = api_client.delete_project(project_id)
        assert cleanup_response.status_code in [200, 204, 404]

    def test_get_project_positive(self, created_project, api_client):
        project_id = created_project["id"]

        response = api_client.get_project(project_id)

        assert api_client.is_successful_response(response, [200]), (
            f"Expected 200, got {response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

        response_data = response.json()
        assert response_data["id"] == project_id

    def test_update_project_positive(self, created_project, api_client):
        project_id = created_project["id"]
        updated_data = {
            "title": "Updated Test Project"
        }
        response = api_client.update_project(project_id, updated_data)

        assert api_client.is_successful_response(response, [200]), (
            f"Expected 200, got {response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

        response_data = response.json()
        assert response_data["id"] == project_id

    def test_create_multiple_projects(self, api_client, project_cleanup_list):
        projects_to_create = [
            {
                "title": f"Batch Project 1 {uuid.uuid4().hex[:6]}"
            },
            {
                "title": f"Batch Project 2 {uuid.uuid4().hex[:6]}"
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
            "users": {}
        }
        response = api_client.create_project(invalid_data)

        assert api_client.is_successful_response(response, [400, 422]), (
            f"Expected 400 or 422 for missing title, got "
            f"{response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

    def test_create_project_negative_invalid_data(self, api_client):
        invalid_data = {
            "title": ""
        }
        response = api_client.create_project(invalid_data)

        assert api_client.is_successful_response(response, [400, 422]), (
            f"Expected 400 or 422 for invalid data, got "
            f"{response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

    def test_get_project_negative_nonexistent_id(self, api_client):
        nonexistent_id = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"

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
        nonexistent_id = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
        update_data = {"title": "Updated title"}

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
            "invalid_field": "invalid_value"
        }

        response = api_client.update_project(project_id, invalid_update_data)

        assert api_client.is_successful_response(response, [200, 400, 422]), (
            f"Expected 200, 400 or 422 for update with invalid field, got "
            f"{response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )

    def test_delete_project_negative_nonexistent_id(self, api_client):
        nonexistent_id = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"

        response = api_client.delete_project(nonexistent_id)
        assert api_client.is_successful_response(response, [200, 204, 404]), (
            f"Expected 200, 204 or 404 for nonexistent project deletion, "
            f"got {response.status_code}. "
            f"Error: {api_client.get_error_message(response)}"
        )
