from typing import List

def circularArrayLoop(nums: List[int]) -> bool:
    n = len(nums)
    
    if nums is None or n < 2: return False

    for i in range(0, n):
        if nums[i] == 0: return False

        # s = slow pointer and f = fast pointer
        s, f = i, follow(nums, i)

        # Check if loop is moving in single direction
        while nums[f] * nums[i] > 0 and nums[i] * nums[follow(nums, f)] > 0:
            # If slow is equal to fast pointers
            if s == f:
                # and there is more than one element in the loop
                if s == follow(nums, s): break
                return True
            
            # Increment slow and fast pointers
            s = follow(nums, s)
            f = follow(nums, follow(nums, f))

        s = i
        while nums[s] * nums[i] > 0:
            nums[s], s = 0, follow(nums, s)

    return False

def follow(nums: List[int], i: int) -> int:
    return (len(nums) + nums[i] + i) % len(nums)

inp = [-1]
assert not circularArrayLoop(inp)

inp = [1, 1]
assert circularArrayLoop(inp)

inp = [2,-1,1,2,2]
assert circularArrayLoop(inp)

inp = [-1,2]
assert not circularArrayLoop(inp)

inp = [-2,1,-1,-2,-2]
assert not circularArrayLoop(inp)
