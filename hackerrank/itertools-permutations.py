from itertools import permutations

if __name__ == "__main__":
    in1 = raw_input()
    S, k = in1.split()
    k = int(k)

    l = list(S)
    perm = list(permutations(l, k))

    res = []
    for i in perm:
        res.append("".join(i))
    res.sort()
    for i in res:
        print(i)
