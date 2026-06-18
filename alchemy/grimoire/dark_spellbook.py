from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    response = validate_ingredients(ingredients=ingredients)
    if response.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({response})"
    else:
        return f"Spell rejected: {spell_name} ({response})"
