# Longest Consecutive Sequence
# Medium
# Topics
# Company Tags
# Hints
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7

nums = []
def longest(nums):
    if nums == []:
        return 0
    check = sorted(nums)
    en = 1
    maximum = 1 
    for i in range(1, len(check)):  
        if check[i] == check[i-1] + 1:
            en +=1
            maximum = max(maximum, en)
        elif check[i] != check[i-1]:
            en = 1
    return maximum

print(longest(nums))



# вот самая быстрая реализация 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l=1
        main = 1
        nums.sort()
        print(nums)
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i]+1 == nums[i+1]:
                l += 1
                print(nums[i], l)
            else:
                if l > main:
                    main = l
                l = 1
        if l > main:
            main = l
        return main
        

        # проверка отличается тем что фор делаеют с нулевого и последний проход не делается так как проверяется нынещний и будущий элемент а не прошлый
        # если совпадает, то скипается проход через continue
        # если +1 к нынещнему совпадает с будущем то плюсуется
        # а так схоже дальше, отличается тем что значение максимума сравнивается при сбросе и при выходе из фора, а не при каждой проверке