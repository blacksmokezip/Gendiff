import json


def render(diff: dict) -> str:
    return json.dumps(diff)
