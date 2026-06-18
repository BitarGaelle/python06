def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    response = validate_ingredients(ingredients=ingredients)
    if response.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({response})"
    elif response.endswith("INVALID"):
        return f"Spell rejected: {spell_name} ({response})"
