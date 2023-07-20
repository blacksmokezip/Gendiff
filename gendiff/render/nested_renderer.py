from gendiff.constants import (NESTED, UNCHANGED, REMOVED, ADDED, CHANGED)
from gendiff.render.value_change import value_change


operator = {
    ADDED: "{ws}+ {k}: {v}\n",
    REMOVED: "{ws}- {k}: {v}\n",
    UNCHANGED: "{ws}  {k}: {v}\n",
    CHANGED: "{ws}- {k}: {v1}\n{ws}+ {k}: {v2}\n",
    NESTED: "  {ws}{k}: {op_br}\n{v}{cl_br}\n"
}


def render(diff):
    result = rendering(diff, indent=2)
    return '{\n' + result + '}'


def value_render(value, indent):
    if isinstance(value, dict):
        tmp = []
        w_spaces = ''.rjust(indent + 6)
        for k, v in value.items():
            if isinstance(v, dict):
                ln = f'{w_spaces}{k}: {value_render(v, indent+4)}\n'
                tmp.append(ln)
            else:
                ln = f'{w_spaces}{k}: {v}\n'
                tmp.append(ln)
        return '{\n' + ''.join(tmp) + '}'.rjust(indent + 3)
    else:
        return value


def rendering(diff, indent=1):
    diff = value_change(diff)

    lines = []
    ws = ''.rjust(indent)
    for key, value in diff.items():
        status = value[0]
        if status == NESTED:
            line = rendering(value[1], indent + 4)
            line = operator[status].format(
                ws=ws,
                k=key,
                op_br='{',
                v=line,
                cl_br='}'.rjust(indent + 3)
            )
        elif status == CHANGED:
            first = value_render(value[1], indent)
            second = value_render(value[2], indent)
            line = operator[status].format(
                ws=ws,
                k=key,
                v1=first,
                v2=second
            )
        else:
            new_value = value_render(value[1], indent)
            line = operator[status].format(
                ws=ws,
                k=key,
                v=new_value
            )
        lines.append(line)
    return ''.join(lines)
