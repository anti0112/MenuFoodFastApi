import math
import pytest_asyncio
import pytest


@pytest.mark.asyncio
class TestDishes:
    @pytest_asyncio.fixture
    async def base_url(self, async_client):
        base_url = "/api/v1/menus/"
        new_menu = {
            "title": "My menu 1",
            "description": "My menu description 1"
        }
        response = await async_client.post(base_url, json=new_menu)
        menu_id = response.json()['id']

        url = f"/api/v1/menus/{menu_id}/submenus/"
        new_submenu = {
            "title": "My dish 1",
            "description": "My dish description 1"
        }
        response = await async_client.post(url, json=new_submenu)
        submenu_id = response.json()['id']

        return f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/"

    async def test_empty_dishes(self, async_client, base_url):
        response = await async_client.get(base_url)
        assert response.status_code == 200
        expected_answer = []
        assert expected_answer == response.json()

    async def test_dish_create(self, async_client, base_url):
        new_dish = {
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": 12.50
        }
        response = await async_client.post(base_url, json=new_dish)

        assert response.status_code == 201

        expected_answer = {
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": 12.50
        }
        response_dict = response.json()
        assert expected_answer["title"] == response_dict["title"]
        assert expected_answer["description"] == response_dict["description"]
        assert math.isclose(
            expected_answer["price"], float(response_dict["price"]))

    async def test_detailed_dish(self, async_client, base_url):
        new_dish = {
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": 12.50
        }
        response = await async_client.post(base_url, json=new_dish)

        id = response.json()['id']
        url = base_url + id

        response = await async_client.get(url)
        expected_answer = {
            "title": "My dish 1",
            "description": "My dish description 1",
            "id": id,
        }
        response_dict = response.json()
        assert response.status_code == 200
        assert expected_answer["title"] == response_dict["title"]
        assert expected_answer["description"] == response_dict["description"]
        assert expected_answer["id"] == response_dict["id"]

    async def test_detailed_dish_invalid(self, async_client, base_url):
        new_dish = {
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": 12.50
        }
        response = await async_client.post(base_url, json=new_dish)

        id = response.json()['id']
        url = base_url + (id + '1')

        response = await async_client.get(url)
        assert response.status_code == 404
        
    async def test_patch_dish(self, async_client, base_url):
        new_dish = {
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": 12.50
        }
        response_post = await async_client.post(base_url, json=new_dish)

        id = response_post.json()['id']

        url = base_url + id
        updated_dish = {
            "title": "updated My dish 1",
            "description": "updated My dish description 1",
            'price': 12.50
        }
        response = await async_client.patch(url, json=updated_dish)
        expected_answer = {
            "title": "updated My dish 1",
            "description": "updated My dish description 1",
            "id": id,
        }
        response_dict = response.json()
        assert response.status_code == 200
        assert expected_answer["title"] == response_dict["title"]
        assert expected_answer["description"] == response_dict["description"]
        assert expected_answer["id"] == response_dict["id"]

    async def test_patch_dish_invalid(self, async_client, base_url):
        new_dish = {
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": 12.50
        }
        response_post = await async_client.post(base_url, json=new_dish)

        id = response_post.json()['id']
        url = base_url + (id + '1')

        updated_dish = {
            "title": "updated My dish 1",
            "description": "updated My dish description 1",
            'price': 12.50
        }
        response = await async_client.patch(url, json=updated_dish)
        assert response.status_code == 404

    async def test_delete_dish(self, async_client, base_url):
        new_dish = {
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": 12.50
        }
        response = await async_client.post(base_url, json=new_dish)

        last_uuid = response.json()['id']
        url = base_url + last_uuid

        response = await async_client.delete(url)
        expected_answer = {
            'status': True,
            'message': 'The dish has been deleted'
        }
        assert response.status_code == 200
        assert expected_answer == response.json()

    async def test_delete_dish_invalid(self, async_client, base_url):
        new_dish = {
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": 12.50
        }
        response = await async_client.post(base_url, json=new_dish)

        id = response.json()['id']
        url = base_url + (id + '1')

        response = await async_client.delete(url)
        assert response.status_code == 404

    