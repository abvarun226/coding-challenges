def isCryptSolution(crypt, solution):
    t = tuple(c.translate(str.maketrans(dict(solution))) for c in crypt)
    any_zeros = any(v[0] == '0' for v in t if len(v) > 1)
    return not ((int(t[0]) + int(t[1]) != int(t[2])) or any_zeros)

crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
assert isCryptSolution(crypt, solution), "Test (1) Failed: Should be True"

crypt = ["TEN", "TWO", "ONE"]
solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
assert not isCryptSolution(crypt, solution), "Test (2) Failed: Should be False"

crypt = ["A", "A", "A"]
solution = [["A", "0"]]
assert isCryptSolution(crypt, solution), "Test (3) Failed: Should be True"