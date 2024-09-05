"""
Kochbuch
"""
import json


# Dein Code kommt hier hin

def adjust_recipe(full_recipe, num_servings):
    factor_serving = num_servings / full_recipe['servings']
    adjusted_amount = {}
    for ingredient, amount in full_recipe['ingredients'].items():
        adjusted_amount[ingredient] = amount * factor_serving
    new_recipe = {
        'title': full_recipe['title'],
        'ingredients': adjusted_amount,
        'servings': num_servings
    }
    return new_recipe


def load_recipe(new_json):
    return json.loads(new_json)


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, ' \
                  '"Minced Meat": 500}, "servings": 4} '
    # Dein Code kommt hier hin
    original_recipe = load_recipe(recipe_json)

    adjusted_recipe = adjust_recipe(original_recipe, 2)
    print(adjusted_recipe)
