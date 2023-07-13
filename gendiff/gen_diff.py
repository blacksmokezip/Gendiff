from gendiff.open import open_file
from gendiff.constants import (ADDED, CHANGED, NESTED, REMOVED, UNCHANGED)
from collections import OrderedDict
from gendiff.render import nested_renderer


def gendiff(file1, file2):
    diff = {}

    first_keys = set(file1.keys())
    second_keys = set(file2.keys())

    removed = first_keys.difference(second_keys)
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
        renderer=nested_renderer
):
    f1 = open_file(file1)
    f2 = open_file(file2)
    diff = gendiff(f1, f2)
    return renderer.render(diff)
