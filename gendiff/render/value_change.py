def value_change(items):
    for key in items:
        temp = list(items[key])
        for i, item in enumerate(temp):
            if item is True:
                temp[i] = 'true'
            elif item is False:
                temp[i] = 'false'
            elif item is None:
                temp[i] = 'null'
        items[key] = tuple(temp)
    result = items
    return result
