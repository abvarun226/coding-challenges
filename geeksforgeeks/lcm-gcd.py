def gcd(a, b):
    if b > 0:
        return gcd(b, a % b)
    else:
        return a

t = int(input())
for _ in range(0, t):
    a, b = map(int, input().split())
    if a > b:
        gcdres = gcd(a, b)
    else:
        gcdres = gcd(b, a)
    lcmres = (a * b) // gcdres
    print(lcmres, gcdres)