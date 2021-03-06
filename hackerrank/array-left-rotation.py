def rotationUsingGCD(a, d):
    ''' Most optimal: time O(n) and space O(1) '''
    n = len(a)
    for i in range(gcd(d, n)):
        current = i
        temp = a[current]
        while True:
            nextElem = current + d - n if current + d >= n else current + d
            if nextElem == i: break
            a[current] = a[nextElem]
            current = nextElem
        a[current] = temp
    return a

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def rotation(a, d):
    ''' Optimal with extra space: time O(n) and space O(d) '''
    d = d % len(a)
    return a[d:] + a[:d]

inp = [
    ("1 2 3 4 5 6 7 8 9 10 11 12", 3, "4 5 6 7 8 9 10 11 12 1 2 3"),
    ("1 2 3 4 5", 4, "5 1 2 3 4"),
    ("0 1 2 3 4 5 6", 2, "2 3 4 5 6 0 1"),
    ("431 397 149 275 556 362 852 789 601 357 516 575 670 507 127 888 284 405 806 27 495 879 976 467 342 356 908 750 769 947 425 643 754 396 653 595 108 75 347 394 935 252 683 966 553 724 629 567 93 494 693 965 328 187 728 389 70 288 509 252 449", 48, "93 494 693 965 328 187 728 389 70 288 509 252 449 431 397 149 275 556 362 852 789 601 357 516 575 670 507 127 888 284 405 806 27 495 879 976 467 342 356 908 750 769 947 425 643 754 396 653 595 108 75 347 394 935 252 683 966 553 724 629 567"),
    ("41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51", 10, "77 97 58 1 86 58 26 10 86 51 41 73 89 7 10 1 59 58 84 77"),
    ("0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19", 10, "10 11 12 13 14 15 16 17 18 19 0 1 2 3 4 5 6 7 8 9")
]

for i, v in enumerate(inp):
    a = list(map(int, v[0].split()))
    d = v[1]
    r = rotation(a, d)
    assert v[2] == ' '.join(map(str, r)), f"failed for input {i+1}"
