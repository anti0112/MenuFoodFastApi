import pytest
from starlette.testclient import TestClient


class TestSubmenu:
    @pytest.fixture(scope="class")
    def base_url(self, test_client: TestClient, test_db):
        base_url = "/api/v1/menus/"
        new_menu = {
            "title": "My menu 1",
            "description": "My menu description 1"
        }
        response = test_client.post(base_url, json=new_menu)
        menu_id = response.json()['id']
        return f"/api/v1/menus/{menu_id}/submenus/"

    def test_empty_submenus(self, test_client: TestClient, test_db, base_url):
        response = test_client.get(base_url)
        assert response.status_code == 200
        expected_answer = []
        assert expected_answer == response.json()

    def test_submenu_create(self, test_client: TestClient, test_db, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1"
        }
        response = test_client.post(base_url, json=new_submenu)

        assert response.status_code == 201

        expected_answer = {
            "title": "My submenu 1",
            "description": "My submenu description 1",
        }
        response_dict = response.json()
        assert expected_answer["title"] == response_dict["title"]
        assert expected_answer["description"] == response_dict["description"]
        assert isinstance(response_dict["id"], str)

    def test_detailed_submenu(self, test_client: TestClient, test_db, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1"
        }
        response = test_client.post(base_url, json=new_submenu)

        id = response.json()['id']
        url = base_url + id

        response = test_client.get(url)
        expected_answer = {
            "title": "My submenu 1",
            "description": "My submenu description 1",
            "dishes_count": 0,
            "id": id,
        }
        response_dict = response.json()
        assert response.status_code == 200
        assert expected_answer["title"] == response_dict["title"]
        assert expected_answer["description"] == response_dict["description"]
        assert expected_answer["dishes_count"] == response_dict["dishes_count"]
        assert expected_answer["id"] == response_dict["id"]

    def test_detailed_submenu_invalid(self, test_client: TestClient, test_db, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1"
        }
        response = test_client.post(base_url, json=new_submenu)

        id = response.json()['id']
        url = base_url + (id+'1')

        response = test_client.get(url)
        assert response.status_code == 404

    def test_delete_submenu(self, test_client: TestClient, test_db, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1"
        }
        response = test_client.post(base_url, json=new_submenu)

        id = response.json()['id']
        url = base_url + id

        response = test_client.delete(url)
        expected_answer = {
            'message': 'The submenu has been deleted',
            'status': 'true'
        }
        assert response.status_code == 200
        assert expected_answer == response.json()

    def test_delete_submenu_invalid(self, test_client: TestClient, test_db, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1"
        }
        response = test_client.post(base_url, json=new_submenu)

        id = response.json()['id']
        url = base_url + (id+'1')

        response = test_client.delete(url)
        assert response.status_code == 404

    def test_patch_submenu(self, test_client: TestClient, test_db, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1"
        }
        response = test_client.post(base_url, json=new_submenu)

        id = response.json()['id']

        url = base_url + id
        updated_submenu = {
            "title": "updated My submenu 1",
            "description": "updated My submenu description 1"
        }
        response = test_client.patch(url, json=updated_submenu)
        expected_answer = {
            "title": "updated My submenu 1",
            "description": "updated My submenu description 1",
            "id": id,
        }
        response_dict = response.json()
        assert response.status_code == 200
        assert expected_answer["title"] == response_dict["title"]
        assert expected_answer["description"] == response_dict["description"]
        assert expected_answer["id"] == response_dict["id"]

    def test_patch_submenu_invalid(self, test_client: TestClient, test_db, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1"
        }
        response = test_client.post(base_url, json=new_submenu)

        id = response.json()['id']
        url = base_url + (id+'1')

        updated_submenu = {
            "title": "updated My submenu 1",
            "description": "updated My submenu description 1"
        }
        response = test_client.patch(url, json=updated_submenu)
        assert response.status_code == 404