import pytest
import pytest_asyncio


@pytest.mark.asyncio
class TestSubmenu:
    @pytest_asyncio.fixture
    async def base_url(self, async_client):
        base_url = "/api/v1/menus/"
        new_menu = {
            "title": "My menu 1",
            "description": "My menu description 1",
        }
        response = await async_client.post(base_url, json=new_menu)
        menu_id = response.json()["id"]
        return f"/api/v1/menus/{menu_id}/submenus/"

    async def test_empty_submenus(self, async_client, base_url):
        response = await async_client.get(base_url)
        assert response.status_code == 200
        expected_answer = []
        assert expected_answer == response.json()

    async def test_submenu_create(self, async_client, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1",
        }
        response = await async_client.post(base_url, json=new_submenu)

        assert response.status_code == 201

        expected_answer = {
            "title": "My submenu 1",
            "description": "My submenu description 1",
        }
        response_dict = response.json()
        assert expected_answer["title"] == response_dict["title"]
        assert expected_answer["description"] == response_dict["description"]
        assert isinstance(response_dict["id"], str)

    async def test_detailed_submenu(self, async_client, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1",
        }
        response = await async_client.post(base_url, json=new_submenu)

        id = response.json()["id"]
        url = base_url + id

        response = await async_client.get(url)
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

    async def test_detailed_submenu_invalid(self, async_client, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1",
        }
        response = await async_client.post(base_url, json=new_submenu)

        id = response.json()["id"]
        url = base_url + (id + "1")

        response = await async_client.get(url)
        assert response.status_code == 404

    async def test_delete_submenu(self, async_client, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1",
        }
        response = await async_client.post(base_url, json=new_submenu)

        id = response.json()["id"]
        url = base_url + id

        response = await async_client.delete(url)
        expected_answer = {
            "message": "The submenu has been deleted",
            "status": True,
        }
        assert response.status_code == 200
        assert expected_answer == response.json()

    async def test_delete_submenu_invalid(self, async_client, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1",
        }
        response = await async_client.post(base_url, json=new_submenu)

        id = response.json()["id"]
        url = base_url + (id + "1")

        response = await async_client.delete(url)
        assert response.status_code == 404

    async def test_patch_submenu(self, async_client, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1",
        }
        response = await async_client.post(base_url, json=new_submenu)

        id = response.json()["id"]

        url = base_url + id
        updated_submenu = {
            "title": "updated My submenu 1",
            "description": "updated My submenu description 1",
        }
        response = await async_client.patch(url, json=updated_submenu)
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

    async def test_patch_submenu_invalid(self, async_client, base_url):
        new_submenu = {
            "title": "My submenu 1",
            "description": "My submenu description 1",
        }
        response = await async_client.post(base_url, json=new_submenu)

        id = response.json()["id"]
        url = base_url + (id + "1")

        updated_submenu = {
            "title": "updated My submenu 1",
            "description": "updated My submenu description 1",
        }
        response = await async_client.patch(url, json=updated_submenu)
        assert response.status_code == 404
