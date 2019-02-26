t = int(input())
for _ in range(0, t):
    n, m = map(int, input().split())
    d = n // m

    if abs(n - (m * d)) < abs(((d + 1) * m) - n):
        print(m * d)
    elif abs(n - (m * d)) > abs(((d + 1) * m) - n):
        print((d + 1) * m)
    else:
        if abs(m * d) > abs(((d + 1) * m)):
            print(m * d)
        else:
            print((d + 1) * m)