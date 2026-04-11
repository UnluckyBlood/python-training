class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
        for i in range(len(s)):
            if s[i] != s[-i-1]: return False
        return True
sol = Solution()
str = "caT tac%^&*?"
print (sol.isPalindrome(str))
