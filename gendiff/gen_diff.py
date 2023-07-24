from gendiff.parser import parse
from gendiff.constants import (ADDED, CHANGED, NESTED, REMOVED, UNCHANGED)
from collections import OrderedDict
from gendiff.render import nested_renderer, plain_renderer, json_renderer


render_map = {
    'stylish': nested_renderer,
    'plain': plain_renderer,
    'json': json_renderer,
    'nested': nested_renderer
}


def gendiff(before_dict, after_dict):
    diff = {}

    first_keys = set(before_dict.keys())
    second_keys = set(after_dict.keys())

    removed = first_keys.difference(after_dict)
    for key in removed:
        diff[key] = (REMOVED, before_dict[key])

    added = second_keys.difference(first_keys)
    for key in added:
        diff[key] = (ADDED, after_dict[key])

    for key in first_keys.intersection(second_keys):
        old_value = before_dict[key]
        new_value = after_dict[key]
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
    before_dict = parse(file1)
    after_dict = parse(file2)
    diff = gendiff(before_dict, after_dict)
    renderer = render_map[renderer]
    return renderer.render(diff)
