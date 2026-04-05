# Групповые Анаграммы
# Medium
# Темы
# Теги компании
# Подсказки
# Дан массив строк strs, сгруппируйте все анаграммы в подсписки. Вы можете вернуть результат в любом порядке.

# Анаграмма — это строка, в которой те же символы, что и в другой строке, но порядок символов может быть другим.

# Пример 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Пример 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Пример 3:

# Input: strs = [""]

# Output: [[""]]
# Ограничения:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] состоит из строчных букв английского алфавита.

def groupAnagrams(strs):
    d = {}
    for s in strs:
        d.setdefault(''.join(sorted(s)), []).append(s)
    return list(d.values())