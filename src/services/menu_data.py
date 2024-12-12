import csv
from typing import Set, Dict, List
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes: Set[Dish] = set()
        self.load_data()

    def load_data(self) -> None:
        with open(self.source_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            dish_dict: Dict[str, Dish] = {}

            for row in reader:
                dish_name = row['dish']
                price = float(row['price'])
                ingredient_name = row['ingredient']
                amount = int(row['recipe_amount'])

                # Cria ou obtém o prato
                if dish_name not in dish_dict:
                    dish_dict[dish_name] = Dish(dish_name, price)

                # Cria o ingrediente
                ingredient = Ingredient(ingredient_name)

                # Adiciona o ingrediente ao prato
                dish_dict[dish_name].add_ingredient_dependency(ingredient, amount)

            # Adiciona todos os pratos ao conjunto de pratos
            self.dishes.update(dish_dict.values())

    def count_unique_ingredients(self) -> Set[str]:
        unique_ingredients = set()
        for dish in self.dishes:
            for ingredient in dish.get_ingredients():
                unique_ingredients.add(ingredient.name)
        return unique_ingredients

    def get_dishes(self) -> Set[Dish]:
        return self.dishes

    def get_dish_restrictions(self, dish_name: str) -> Set:
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish.get_restrictions()
        return set()
