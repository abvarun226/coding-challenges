def plusOne(A):
    n = len(A)
    carry = 0
    incr = 1
    B = ""
    for i in range(n-1, -1, -1):
        x = A[i] + incr + carry
        incr = 0
        B = str(x % 10) + B
        carry = 0
        if x > 9:
            carry = 1
    if carry > 0:
        B = str(carry) + B
    return list(map(int, list(B.lstrip("0"))))

print(plusOne([0, 9, 9, 9, 9]))
print(plusOne([0, 9, 9, 9, 8]))
print(plusOne([1, 2, 9]))
print(plusOne([1, 2, 8]))