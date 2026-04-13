# Допустимый Палиндром
# Легко
# Темы
# Теги компании
# Подсказки
# Для заданной строки s верните true в случае, если она является палиндромом, в противном случае верните false.

# Палиндром — это строка, которая читается одинаково как слева направо, так и справа налево. Она не учитывает регистр и игнорирует все небуквенно-цифровые символы.

# Примечание: буквенно-цифровые символы состоят из букв (A-Z, a-z) и цифр (0-9).

# Пример 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Пояснение: если рассматривать только буквенно-цифровые символы, то получится «wasitacaroracatisaw», что является палиндромом.

# Пример 2:

# Input: s = "tab a cat"

# Output: false
# Пояснение: "tabacat" не является палиндромом.

# Ограничения:

# 1 <= s.length <= 1000
# s состоит только из печатных символов ASCII.

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
