from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
from numbers import Real
import pytest


def test_dish():
    # Setup: Criação dos pratos
    dish = Dish("lasanha de presunto", 25.9)
    dish2 = Dish("lasanha de presunto", 25.9)
    dish3 = Dish("lasanha de beringela", 27.0)

    # Teste de inicialização
    assert dish.name == "lasanha de presunto"
    assert dish.price == 25.9
    assert dish.recipe == {}

    # Teste de representação
    assert repr(dish) == "Dish('lasanha de presunto', R$ 25.90)"

    # Teste de igualdade
    assert dish == dish2
    assert dish != dish3

    # Teste de hash
    assert hash(dish) == hash(dish2)
    assert hash(dish) != hash(dish3)

    # Adicionando ingredientes
    lasanha = Ingredient("massa de lasanha")
    presunto = Ingredient("presunto")
    amount = 15
    Dish.add_ingredient_dependency(dish, lasanha, amount)
    Dish.add_ingredient_dependency(dish, presunto, amount)

    # Teste de ingredientes
    assert set(Dish.get_ingredients(dish)) == {lasanha, presunto}

    # Teste de restrições
    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.GLUTEN,
        Restriction.ANIMAL_MEAT
    }
    assert Dish.get_restrictions(dish) == expected_restrictions

    # Teste de preço inválido
    with pytest.raises(ValueError, match="Dish price must be greater than zero."):
        Dish("lasanha de presunto", 0)

    # Teste de tipo de preço inválido
    invalid_dish = Dish("lasanha de presunto", 2)
    assert isinstance(invalid_dish.price, Real), "Dish price must be float."
