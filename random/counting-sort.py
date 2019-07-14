def sort(a):
    n = len(a)
    k = max(a) + 1
    pos = [0] * k
    for v in a:
        pos[v] += 1

    s = 0
    for i in range(0, k):
        temp = pos[i]
        pos[i] = s
        s += temp

    out = [None] * n
    for v in a:
        out[pos[v]] = v
        pos[v] = pos[v] + 1

    return out


samples = [
    [4, 1, 3, 2, 3],
    [8, 0, 1, 3, 4, 10],
    [1, 1, 1],
    [10]
]

for a in samples:
    res = sort(a)
    assert res == sorted(a), f"incorrect sort {res}"