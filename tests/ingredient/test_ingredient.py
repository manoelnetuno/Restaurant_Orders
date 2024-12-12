from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    # Setup: Criação dos ingredientes
    ingredient = Ingredient('camarão')
    ingredient2 = Ingredient('creme de leite')
    ingredient3 = Ingredient('camarão')

    # Teste de inicialização
    assert ingredient.name == 'camarão'
    assert ingredient.restrictions == {Restriction.SEAFOOD}

    # Teste de representação
    assert repr(ingredient2) == "Ingredient('creme de leite')"

    # Teste de igualdade
    assert ingredient == ingredient3
    assert ingredient != ingredient2

    # Teste de hash
    assert hash(ingredient) == hash(ingredient3)
    assert hash(ingredient) != hash(ingredient2)
