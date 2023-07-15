from gendiff.constants import CHANGED, UNCHANGED, NESTED, ADDED, REMOVED


constants = {
    ADDED: "was added with value: {0}",
    REMOVED: "was removed",
    CHANGED: "was updated. From {0} to {1}",
    UNCHANGED: ""
}


def render(diff, path=''):
    lines = []
    temp_str = "Property '{path}' {line}\n"
    for key, value in diff.items():
        status = value[0]
        if status == NESTED:
            line = render(value[1], path + f'{key}.')
            lines.append(line)
        elif status == UNCHANGED:
            continue
        else:
            temp = complex_values(value[1:])
            for i, v in enumerate(temp):
                if v != 'false'\
                        and v != 'true'\
                        and v != 'null'\
                        and v != '[complex value]':
                    temp[i] = f"'{v}'"
            line = constants[status].format(*temp)
            lines.append(
                temp_str.format(
                    path=path + f'{key}',
                    line=line
                )
            )
    return ''.join(lines)


def complex_values(values):
    new = []
    for v in values:
        if isinstance(v, dict):
            v = '[complex value]'
        new.append(v)
    return new
