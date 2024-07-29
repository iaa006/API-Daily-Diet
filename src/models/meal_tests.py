import pytest
from src.models.meal import Meal

@pytest.mark.skip(reason='interation with the db')
def test_create_meal():
    new_meal = Meal(name='Breakfast', description='Cuscuz with meat', date_time='21/07/2024 08:30', on_diet=False)

    new_meal.create_meal()

