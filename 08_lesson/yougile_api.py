import requests
import os
from typing import Dict, Any, Optional, List


class YougileAPI:

    def __init__(self):
        self.base_url = "https://yougile.com"
        self.token = os.getenv("YOUGILE_TOKEN")
        if not self.token:
            raise ValueError(
                "YOUGILE_TOKEN environment variable is required. "
                "Please set it with your API token from yougile.com"
            )

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def _make_request(self, method: str, endpoint: str,
                      data: Optional[Dict[str, Any]] = None
                      ) -> requests.Response:
        url = f"{self.base_url}{endpoint}"

        try:
            if method.upper() == "GET":
                return requests.get(url, headers=self.headers)
            elif method.upper() == "POST":
                return requests.post(url, headers=self.headers, json=data)
            elif method.upper() == "PUT":
                return requests.put(url, headers=self.headers, json=data)
            elif method.upper() == "DELETE":
                return requests.delete(url, headers=self.headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def _validate_project_data(self, project_data: Dict[str, Any]) -> None:
        if not isinstance(project_data, dict):
            raise ValueError("Project data must be a dictionary")

        if "title" in project_data and not project_data["title"]:
            raise ValueError("Project title cannot be empty")

    def _validate_project_id(self, project_id: str) -> None:
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")

    def is_successful_response(self, response: requests.Response,
                               expected_codes: List[int]) -> bool:
        return response.status_code in expected_codes

    def get_error_message(self, response: requests.Response) -> str:
        try:
            error_data = response.json()
            return error_data.get("message", f"HTTP {response.status_code}")
        except Exception:
            return f"HTTP {response.status_code}: {response.text}"

    def create_project(self, project_data: Dict[str, Any]
                       ) -> requests.Response:
        self._validate_project_data(project_data)
        return self._make_request("POST", "/api-v2/projects", project_data)

    def update_project(self, project_id: str,
                       project_data: Dict[str, Any]) -> requests.Response:
        self._validate_project_id(project_id)
        self._validate_project_data(project_data)
        return self._make_request("PUT", f"/api-v2/projects/{project_id}",
                                  project_data)

    def get_project(self, project_id: str) -> requests.Response:
        self._validate_project_id(project_id)
        return self._make_request("GET", f"/api-v2/projects/{project_id}")

    def delete_project(self, project_id: str) -> requests.Response:
        self._validate_project_id(project_id)
        return self._make_request("DELETE", f"/api-v2/projects/{project_id}")

    def get_all_projects(self) -> requests.Response:
        return self._make_request("GET", "/api-v2/projects")

    def create_project_and_get_id(self, project_data: Dict[str, Any]) -> str:
        response = self.create_project(project_data)
        if not self.is_successful_response(response, [201]):
            error_msg = self.get_error_message(response)
            raise Exception(f"Failed to create project: {error_msg}")
        return response.json()["id"]

    def project_exists(self, project_id: str) -> bool:
        try:
            response = self.get_project(project_id)
            return self.is_successful_response(response, [200])
        except Exception:
            return False

    def wait_for_project_deletion(self, project_id: str,
                                  max_attempts: int = 3) -> bool:

        import time

        for _ in range(max_attempts):
            if not self.project_exists(project_id):
                return True
            time.sleep(1)

        return False
