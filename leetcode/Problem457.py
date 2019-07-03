from typing import List

def circularArrayLoop(nums: List[int]) -> bool:
    n = len(nums)
    for i in range(0, n):
        s = i
        f = i

        while nums[s] * nums[next(nums, f)] > 0 and nums[s] * nums[next(nums, next(nums, f))] > 0:
            s = next(nums, s)
            f = next(nums, next(nums, f))
            if s == f:
                return not s == next(nums, s)

        j, val = i, nums[i]
        while nums[j] * val > 0:
            j, nums[j] = next(nums, j), 0

    return False

def next(nums: List[int], i: int) -> int:
    return (len(nums) + nums[i] + i) % len(nums)


inp = [2,-1,1,2,2]
assert circularArrayLoop(inp)

inp = [-1,2]
assert not circularArrayLoop(inp)

inp = [-2,1,-1,-2,-2]
assert not circularArrayLoop(inp)
