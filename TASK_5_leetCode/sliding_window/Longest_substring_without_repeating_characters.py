# Самая длинная подстрока без повторяющихся символов
# Medium
# Темы
# Теги компании
# Подсказки
# Дана строка s, найдите длину самой длинной подстроки без повторяющихся символов.

# Подстрока — это непрерывная последовательность символов в строке.

# Пример 1:

# Input: s = "zxyzxyz"

# Output: 3
# Пояснение: строка "xyz" — самая длинная без повторяющихся символов.

# Пример 2:

# Input: s = "xxxx"

# Output: 1
# Ограничения:

# 0 <= s.length <= 1000
# s может состоять из печатных символов ASCII.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        tmp = 0
        stack = []
        for i in range(len(s)):
            if s[i] in stack:
                return_ind = stack.index(s[i])
                for j in range(len(stack)):
                    if j <= return_ind:
                        stack.pop(0)
                        tmp -=1
            stack.append(s[i])
            tmp += 1
            if tmp> max_length: max_length = tmp
        return max_length
    
sol = Solution()
s="dvdf"
print(sol.lengthOfLongestSubstring(s))