# 5. Самая длинная палиндромная подстрока
# Средний
# Темы
# значок премиум-замка
# Компании
# Подсказка
# Для заданной строки s верните самую длинную палиндромную подстроку в s.

 

# Пример 1:

# Входные данные: s = "babad"
# Выходные данные: "bab"
# Пояснение: "aba" тоже является правильным ответом.
# Пример 2:

# Входные данные: s = "cbbd"
# Выходные данные: "bb"
 

# Ограничения:

# 1 <= s.length <= 1000
# s состоят только из цифр и английских букв.








class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        max_len = 1
        n = len(s)

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

        return s[start:start + max_len]