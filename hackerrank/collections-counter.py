from collections import Counter

if __name__ == '__main__':
    X, shoes, N = int(raw_input()), raw_input(), int(raw_input())
    shoes = Counter(map(int, shoes.split()))
    total = 0
    for i in xrange(N):
        t = raw_input()
        s, c = map(int, t.split())
        if s in shoes and shoes[s] > 0:
            total += c
            shoes[s] -= 1
    print(total)
