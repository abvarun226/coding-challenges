"""
https://leetcode.com/problems/3sum/

15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""

def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    n = len(nums)

    for i in range(n-2):
        l = i+1
        r = n-1

        if i > 0 and nums[i] == nums[i-1]:
            continue

        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                result.append([nums[i], nums[l], nums[r]])
                while l < n-1 and nums[l] == nums[l+1]:
                    l += 1
                while r > 0 and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1

    return result

print(threeSum([-1,0,1,2,-1,-4]))