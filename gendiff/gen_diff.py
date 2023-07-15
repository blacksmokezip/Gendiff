from gendiff.open import open_file
from gendiff.constants import (ADDED, CHANGED, NESTED, REMOVED, UNCHANGED)
from collections import OrderedDict
from gendiff.render import nested_renderer, plain_renderer, json_renderer


render_map = {
    'stylish': nested_renderer,
    'plain': plain_renderer,
    'json': json_renderer,
    'nested': nested_renderer
}


def value_change(items):
    for key in items:
        if items[key] is True:
            items[key] = 'true'
        elif items[key] is False:
            items[key] = 'false'
        elif items[key] is None:
            items[key] = 'null'
    result = items
    return result


def gendiff(file1, file2):
    diff = {}

    value_change(file1)
    value_change(file2)

    first_keys = set(file1.keys())
    second_keys = set(file2.keys())

    removed = first_keys.difference(file2)
    for key in removed:
        diff[key] = (REMOVED, file1[key])

    added = second_keys.difference(first_keys)
    for key in added:
        diff[key] = (ADDED, file2[key])

    for key in first_keys.intersection(second_keys):
        old_value = file1[key]
        new_value = file2[key]
        nested = isinstance(old_value, dict) and isinstance(new_value, dict)
        if nested:
            diff[key] = (
                NESTED,
                gendiff(old_value, new_value)
            )
        elif new_value == old_value:
            diff[key] = (UNCHANGED, old_value)
        else:
            diff[key] = (CHANGED, old_value, new_value)

    return OrderedDict(sorted(diff.items(), key=lambda x: x))


def generate_diff(
        file1,
        file2,
        renderer='stylish'
):
    f1 = open_file(file1)
    f2 = open_file(file2)
    diff = gendiff(f1, f2)
    renderer = render_map[renderer]
    return renderer.render(diff)
