def test(*value, end="\n"):
    print(value)
    print(type(value))
    print(end)

    for i in value:
        print(i, end=end)

test('a', 'b', 'c', end="...")