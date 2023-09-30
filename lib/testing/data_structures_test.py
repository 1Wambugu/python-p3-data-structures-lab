# data_structures_test.py

from lib.data_structures import (
    get_names,
    get_spiciest_foods,
    print_spicy_foods,
    get_spicy_food_by_cuisine,
    get_average_heat_level,
    create_spicy_food,
)

def test_get_names():
    spicy_foods = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
    ]
    assert get_names(spicy_foods) == ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

def test_get_spiciest_foods():
    spicy_foods = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
    ]
    expected_result = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
    ]
    assert get_spiciest_foods(spicy_foods) == expected_result

# Add more test cases for other functions as needed...

def test_get_average_heat_level():
    spicy_foods = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
    ]
    assert get_average_heat_level(spicy_foods) == 6

def test_create_spicy_food():
    spicy_foods = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    ]
    new_spicy_food = {"name": "Kimchi", "cuisine": "Korean", "heat_level": 8}
    expected_result = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
        {"name": "Kimchi", "cuisine": "Korean", "heat_level": 8},
    ]
    assert create_spicy_food(spicy_foods, new_spicy_food) == expected_result
