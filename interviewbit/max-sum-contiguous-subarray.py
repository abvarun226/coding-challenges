def maxSumContiguousArray(A):
    max_so_far = 0
    max_here = 0
    neg_so_far = True
    for x in A:
        max_here += x

        if max_here < 0:
            max_here = 0

        if neg_so_far:
            if x > 0:
                neg_so_far = False
            elif max_so_far == 0:
                max_so_far = x
            elif max_so_far <= x:
                max_so_far = x
            continue

        if max_so_far < max_here:
            max_so_far = max_here

    return max_so_far

print(maxSumContiguousArray([-2, -3, 4, -1, -2, 1, 5, -3]))
print(maxSumContiguousArray([-10, -163, -20]))
print(maxSumContiguousArray([-163]))
print(maxSumContiguousArray([-163, 4, 2, 1]))
print(maxSumContiguousArray([-89, -277, -475, -480, -420]))