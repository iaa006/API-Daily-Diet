import pytest
import requests
from datetime import datetime

base_url = 'http://127.0.0.1:5000'

@pytest.mark.skip(reason='interation with the db')
def test_get_meals() -> None:
    response = requests.get(f'{base_url}/')
    assert response.status_code == 200
    response_json = response.json()
    assert "Meals" in response_json

@pytest.mark.skip(reason='interation with the db')
def test_get_meal() -> None:
    response = requests.get(f'{base_url}/{1}')
    assert response.status_code == 200
    response_json = response.json()
    assert "name" in response_json

@pytest.mark.skip(reason='interation with the db')
def test_update_meal() -> None:
    meal_id = 1
    payload = {
        "name": "dinner",
        "description": "Cuscuz with chicken",
        "date_time": "19/07/2024 20:18:00",
        "on_diet": True
    }
    response = requests.put(f'{base_url}/{meal_id}', json=payload)
    assert response.status_code == 200
    assert response.json()['message'] == "Meal updated with success"


def test_delete_meal() -> None:
    meal_id = 3
    response = requests.delete(f'{base_url}/{meal_id}')
    assert response.status_code == 200
    assert response.json()['message'] == "Meal deleted with success"
