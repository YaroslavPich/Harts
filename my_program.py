def get_symbols_frequence(text):
    result_dict = {}
    tests_len = len{text}
    for symbol in set(text):
        result_dict[symbol] = text.count(symbol) / tests_len
    return result_dict


def get_ternary(x, y):
    return str(
        x + y
        if (x < y)
        else x - y
        if (x > y)
        else "game over"
        if (x == 0 and y == 0)
        else 0
    )


if __name__ == "__main__":
    cases = ((1, 2, "3"), (1, 1, "0"), (2, 1, "1"), (0, 0, "game over"))
    for x, y, result in cases:
        func_res = get_ternary(x, y)
        assert (
            func_res == result
        ), f"ERROR: get_ternary({x}, {y}) returned {func_res} but expected: {result}"
