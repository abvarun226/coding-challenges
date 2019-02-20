from collections import defaultdict

if __name__ == '__main__':
    in1 = raw_input()
    n, m = map(int, in1.split())
    A, B = defaultdict(list), []
    for i in xrange(1, n+1):
        A[raw_input()].append(str(i))
    for i in xrange(1, m+1):
        B.append(raw_input())

    for i in B:
        if i in A:
            print(" ".join(A[i]))
        else:
            print("-1")
