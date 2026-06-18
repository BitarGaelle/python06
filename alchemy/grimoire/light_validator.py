
def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    ingred = light_spell_allowed_ingredients()
    parts = [ing.strip().lower() for ing in ingredients.split(",")]
    res = any(ing in parts for ing in ingred)
    if res is True:
        result = "VALID"
    else:
        result = "INVALID"
    return f"{ingredients} - {result}"
