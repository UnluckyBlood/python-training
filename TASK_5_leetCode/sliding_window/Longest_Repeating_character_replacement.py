# Самая длинная повторяющаяся замена символов
# Medium
# Темы
# Теги компании
# Подсказки
# Вам дана строка s, состоящая только из заглавных букв английского алфавита, и целое число k. Вы можете выбрать до k символов в строке и заменить их любым другим заглавным английским символом.

# После выполнения не более k замен верните длину самой длинной подстроки, содержащей только один уникальный символ.

# Пример 1:

# Input: s = "XYYX", k = 2

# Output: 4
# Пояснение: либо замените 'X' на 'Y', либо замените 'Y' на 'X'.

# Пример 2:

# Input: s = "AAABABB", k = 1

# Output: 5
# Ограничения:

# 1 <= s.length <= 1000
# 0 <= k <= s.length



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        count = [0] * 26
        max_count = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0)+1
            max_count = max(max_count, count[s[right]])
            while (right-left+1) - max_count > k:
                count[s[left]] -= 1
                left +=1
            max_len = max(max_len, right-left+1)
            
        return max_len