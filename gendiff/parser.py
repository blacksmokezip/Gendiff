import json
import yaml
import urllib.request


def parse(path):
    if isinstance(path, str) and path.startswith('http'):
        with urllib.request.urlopen(path) as response:
            body_json = response.read()
            return json.loads(body_json)
    with open(path) as f:
        if path.endswith('.yaml') or path.endswith('.yml'):
            return yaml.safe_load(f)
        return json.load(f)
