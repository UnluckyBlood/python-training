# Find Minimum in Rotated Sorted Array
# Medium
# Topics
# Company Tags
# Hints
# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example 1:

# Input: nums = [3,4,5,6,1,2]

# Output: 1
# Example 2:

# Input: nums = [4,5,0,1,2,3]

# Output: 0
# Example 3:

# Input: nums = [4,5,6,7]

# Output: 4
# Constraints:

# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
            

# самый быстрый способ, но он мало отличается по скорости , но при этом если местами одну проверку тут поменять, то он заёмет последнее место по скорости, так что лучше не юз
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1

        res = nums[0]
        while l<=r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            m = (l+r)//2
            res = min(res,nums[m])
            if nums[l] <= nums[m]:
                res = min(nums[l], res)
                l = m+1
            else:
                r = m-1

        return res
    
def check(nums):
    j=0
    for i in range(len(nums)):
        j -=1        
        i = j
        print (i)
nums = [1,2,3,4,5,5, 6,7,5]
check(nums)