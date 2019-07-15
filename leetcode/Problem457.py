from typing import List

def circularArrayLoop(nums: List[int]) -> bool:
    n = len(nums)
    
    if nums is None or n < 2: return False

    for i in range(0, n):
        if nums[i] == 0: return False

        # s = slow pointer and f = fast pointer
        s, f = i, nextElem(nums, i)

        # Check if loop is moving in single direction
        while nums[f] * nums[i] > 0 and nums[i] * nums[nextElem(nums, f)] > 0:
            # If slow is equal to fast pointers
            if s == f:
                # and there is more than one element in the loop
                if s == nextElem(nums, s): break
                return True
            
            # Increment slow and fast pointers
            s = nextElem(nums, s)
            f = nextElem(nums, nextElem(nums, f))

        # mark every index on the path that failed with 0
        s = i
        while nums[s] * nums[i] > 0:
            nums[s], s = 0, nextElem(nums, s)

    return False

def nextElem(nums: List[int], i: int) -> int:
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
