import json


def generate_diff(file1, file2):
    diff = {}

    f1 = json.load(open(file1))
    f2 = json.load(open(file2))

    first_keys = set(f1.keys())
    second_keys = set(f2.keys())

    removed = first_keys.difference(second_keys)
    for key in removed:
        diff[f'- {key}'] = (f1[key])

    added = second_keys.difference(first_keys)
    for key in added:
        diff[f'+ {key}'] = (f2[key])

    for key in first_keys.intersection(second_keys):
        old_value = f1[key]
        new_value = f2[key]
        if new_value == old_value:
            diff[f'  {key}'] = (old_value)
        else:
            diff[f'- {key}'] = (old_value)
            diff[f'+ {key}'] = (new_value)

    result = dict(sorted(diff.items(), key=lambda x: x[0][2:]))
    return result