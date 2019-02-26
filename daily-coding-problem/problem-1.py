# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


def exists(alist, k):
    dicti = {}
    for v in alist:
        # For dictionary (hash table), `in` operator time complexity is O(1)
        if (k - v) in dicti:
            return True
        dicti[v] = True
    return False

if __name__ == '__main__':
    alist = [10, 15, 3, 7]
    k = 17
    print("Does the pair exist? {}".format(exists(alist, k)))