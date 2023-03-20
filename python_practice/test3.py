def test(*value, end="\n", add=""): # type(value) -> tuple
    print(f'value: {value}')
    print(f'type(value): {type(value)}')

    value = list(value)
    print(f'type(list(value)): {type(value)}', f'value: {value}', sep="\n")
    value.append(add)

    print(f'end: {end}')
    print("add: {}".format(add))

    for i in value:
        print(i, end=end)

test('a', 'b', 'c', end="...", add="text")