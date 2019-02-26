import math

def prime_divisors(n):
    divisors = {}
    while n % 2 == 0:
        if 2 not in divisors:
            divisors[2] = 1
        n = n // 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i not in divisors:
                divisors[i] = 1
            n = n // i
    
    if n > 2:
        if n not in divisors:
            divisors[n] = 1
    
    return divisors

def leastCommonPrimeDivisor(a, b):
    a_divisors = prime_divisors(a)
    b_divisors = prime_divisors(b)
    common_divisor = -1
    for k in a_divisors:
        if k in b_divisors and (common_divisor == -1 or common_divisor > k):
            common_divisor = k
    return common_divisor

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(leastCommonPrimeDivisor(a, b))