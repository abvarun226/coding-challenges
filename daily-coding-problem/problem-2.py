def with_division(series):
    product = 1
    for i in series:
        product *= i
    for i, v in enumerate(series):
        series[i] = product // v
    return series

def without_division(series):
    l = [1] * len(series)
    r = [1] * len(series)
    for i in range(1, len(series)):
        l[i] = series[i-1] * l[i-1]
    for i in range(len(series)-2, -1, -1):
        r[i] = series[i+1] * r[i+1] 
    series = [a * b for a, b in zip(l, r)]
    return series

if __name__ == "__main__":
    inp = [1, 2, 3, 4, 5]
    expected = [120, 60, 40, 30, 24]
    result = without_division(inp)
    print(result)
    assert expected == result

    inp = [3, 2, 1]
    expected = [2, 3, 6]
    result = without_division(inp) 
    print(result)
    assert expected == result