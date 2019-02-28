def lowestMissingPositiveInteger_1(series):
    h = {}
    maxval = 0
    for i in series:
        h[i] = True
        if i > maxval:
            maxval = i
    for i in range(1, maxval+1):
        if i not in h:
            return i
    return maxval+1

def lowestMissingPositiveInteger_2(arr):
    n = len(arr)
    for i in range(0, n):
        if arr[i] <= 0 or arr[i] > n:
            continue
        val = arr[i]
        while arr[val-1] != val:
            t = arr[val-1]
            arr[val-1] = val
            val = t
            if val <= 0 or val > n:
                break
    for i in range(0, n):
        if arr[i] != i+1:
            return i+1
    return n+1

if __name__ == '__main__':
    inp = [3, 4, -1, 1]
    exp = 2
    res = lowestMissingPositiveInteger_2(inp)
    assert res == exp

    inp = [1, 2, 0]
    exp = 3
    res = lowestMissingPositiveInteger_2(inp)
    assert res == exp

    inp = [3, 4, -1]
    exp = 1
    res = lowestMissingPositiveInteger_2(inp)
    assert res == exp

    inp = [-3, -4, -1]
    exp = 1
    res = lowestMissingPositiveInteger_2(inp)
    assert res == exp
