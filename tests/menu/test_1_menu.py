import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
class TestMenu:
    base_url = '/api/v1/menus/'

    async def test_get_menus(self, async_client: AsyncClient):
        response = await async_client.get(self.base_url)
        assert response.status_code == 200
        expected_answer = []
        assert expected_answer == response.json()

    async def test_menu_create(self, async_client: AsyncClient):
        new_menu = {
            "title": "My menu 1",
            "description": "My menu description 1"
        }
        response = await async_client.post(self.base_url, json=new_menu)

        assert response.status_code == 201

        expected_answer = {
            "title": "My menu 1",
            "description": "My menu description 1",
        }
        response_dict = response.json()
        assert expected_answer["title"] == response_dict["title"]
        assert expected_answer["description"] == response_dict["description"]
        assert isinstance(response_dict["id"], str)

    async def test_detail_menu(self, async_client):
        new_menu = {
            "title": "My menu 1",
            "description": "My menu description 1"
        }
        response = await async_client.post(self.base_url, json=new_menu)

        id = response.json()['id']
        url = self.base_url + id

        response = await async_client.get(url)
        expected_answer = {
            "title": "My menu 1",
            "description": "My menu description 1",
            "submenus_count": 0,
            "dishes_count": 0,
            "id": id,
        }
        response_dict = response.json()
        assert response.status_code == 200
        assert expected_answer["title"] == response_dict["title"]
        assert expected_answer["description"] == response_dict["description"]
        assert expected_answer["submenus_count"] == response_dict["submenus_count"]
        assert expected_answer["dishes_count"] == response_dict["dishes_count"]
        assert expected_answer["id"] == response_dict["id"]

    async def test_detailed_menu_invalid(self, async_client):
        new_menu = {
            "title": "My menu 1",
            "description": "My menu description 1"
        }
        response = await async_client.post(self.base_url, json=new_menu)

        id = response.json()['id']
        url = self.base_url + (id + '1')

        response = await async_client.get(url)
        assert response.status_code == 404

    async def test_delete_menu(self, async_client):
        new_menu = {
            "title": "My menu 1",
            "description": "My menu description 1"
        }
        response = await async_client.post(self.base_url, json=new_menu)

        id = response.json()['id']
        url = self.base_url + id

        response = await async_client.delete(url)
        expected_answer = {
            'status': True,
            'message': 'The menu has been deleted'
        }
        assert response.status_code == 200
        assert expected_answer == response.json()

    async def test_delete_menu_invalid(self, async_client):
        new_menu = {
            "title": "My menu 1",
            "description": "My menu description 1"
        }
        response = await async_client.post(self.base_url, json=new_menu)

        id = response.json()['id']
        url = self.base_url + (id + '1')

        response = await async_client.delete(url)
        assert response.status_code == 404

    async def test_patch_menu(self, async_client):
        new_menu = {
            "title": "My menu 1",
            "description": "My menu description 1"
        }
        response = await async_client.post(self.base_url, json=new_menu)

        id = response.json()['id']

        url = self.base_url + id
        updated_menu = {
            "title": "updated My menu 1",
            "description": "updated My menu description 1"
        }
        response = await async_client.patch(url, json=updated_menu)
        expected_answer = {
            "title": "updated My menu 1",
            "description": "updated My menu description 1",
            "id": id,
        }
        response_dict = response.json()
        assert response.status_code == 200
        assert expected_answer["title"] == response_dict["title"]
        assert expected_answer["description"] == response_dict["description"]
        assert expected_answer["id"] == response_dict["id"]

    async def test_patch_menu_invalid(self, async_client):
        new_menu = {
            "title": "My menu 1",
            "description": "My menu description 1"
        }
        response = await async_client.post(self.base_url, json=new_menu)

        id = response.json()['id']
        url = self.base_url + (id + '1')

        updated_menu = {
            "title": "updated My menu 1",
            "description": "updated My menu description 1"
        }
        response = await async_client.patch(url, json=updated_menu)
        assert response.status_code == 404
