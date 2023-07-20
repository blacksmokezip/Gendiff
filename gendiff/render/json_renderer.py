import json
from gendiff.render.value_change import value_change


def render(diff: dict) -> str:
    diff = value_change(diff)
    return json.dumps(diff)
