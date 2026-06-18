from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingred = dark_spell_allowed_ingredients()
    parts = [ing.strip().lower for ing in ingredients.split(",")]
    res = any(ing in parts for ing in ingred)
    if res is True:
        result = "VALID"
    else:
        result = "INVALID"
    return f"{ingredients} - {result}"
