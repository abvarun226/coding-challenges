a = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36],
]

n = len(a)
m = n - 1
for x in range(0, int(n/2)):
    c = m
    for y in range(x, m):
        a[x][y], a[y][m], a[m][c], a[c][x] = a[c][x], a[x][y], a[y][m], a[m][c]
        c -= 1
    m -= 1

for i in a:
    print(i)