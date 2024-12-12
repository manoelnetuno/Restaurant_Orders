import csv
from typing import Set, Dict, List


class Ingredient:
    def __init__(self, name: str, quantity: float) -> None:
        self.name = name
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"{self.quantity} of {self.name}"

    def __eq__(self, other) -> bool:
        return isinstance(other, Ingredient) and self.name == other.name and self.quantity == other.quantity

    def __hash__(self) -> int:
        return hash((self.name, self.quantity))


class Dish:
    def __init__(self, name: str, ingredients: List[Ingredient], price: float) -> None:
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __repr__(self) -> str:
        return f"{self.name}: {self.ingredients}, Price: {self.price}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Dish):
            return False
        return self.name == other.name and self.ingredients == other.ingredients and self.price == other.price

    def __hash__(self) -> int:
        return hash((self.name, tuple(self.ingredients), self.price))


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes: Set[Dish] = set()
        self.load_data()

    def load_data(self) -> None:
        with open(self.source_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            dish_dict: Dict[str, List[Ingredient]] = {}
            for row in reader:
                dish_name = row['dish']
                price = float(row['price'])
                ingredient_name = row['ingredient']
                quantity = float(row['recipe_amount'])

                ingredient = Ingredient(ingredient_name, quantity)

                if dish_name not in dish_dict:
                    dish_dict[dish_name] = {'ingredients': [], 'price': price}
                dish_dict[dish_name]['ingredients'].append(ingredient)

            for dish_name, data in dish_dict.items():
                dish = Dish(dish_name, data['ingredients'], data['price'])
                self.dishes.add(dish)

    def count_unique_ingredients(self) -> Set[str]:
        unique_ingredients = set()
        for dish in self.dishes:
            for ingredient in dish.ingredients:
                unique_ingredients.add(ingredient.name)
        return unique_ingredients
