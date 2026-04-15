# Minimum Window Substring
# Hard
# Topics
# Company Tags
# Hints
# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"
# Example 3:

# Input: s = "x", t = "xy"

# Output: ""
# Constraints:

# 1 <= s.length <= 1000
# 1 <= t.length <= 1000
# s and t consist of uppercase and lowercase English letters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for i in t:
            need[i] = need.get(i, 0)+1
        have = {}
        left = 0
        min_len = float('inf')
        min_start = 0
        formed = 0
        required = len(need)

        for right in range(len(s)):
            i = s[right]
            have[i] = have.get(i,0)+1
            if i in need and have[i] == need[i]:
                formed += 1
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                left_char = s[left]
                have[left_char] -= 1
                if left_char in need and  have[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        return s[min_start:min_start+min_len] if min_len != float('inf') else ""
    

sol = Solution()
str_s = "ADOBECODEBANC"
str_t = "ABC"
print (sol.minWindow(str_s,str_t))