
# 6. Зигзагообразная конверсия
# Решено
# Средний
# Темы
# значок премиум-замка
# Компании
# Строка "PAYPALISHIRING" записывается зигзагом в заданном количестве строк следующим образом: (для лучшей читаемости можно отобразить этот узор фиксированным шрифтом)

# П А Х Н
# А П Л С И И Г
# Й И Р
# А затем читайте построчно: "PAHNAPLSIIGYIR"

# Напишите код, который будет принимать строку и выполнять это преобразование для заданного количества строк:

# string convert(string s, int numRows);
 

# Пример 1:

# Входные данные: s = "PAYPALISHIRING", numRows = 3
# Выходные данные: "PAHNAPLSIIGYIR"
# Пример 2:

# Входные данные: s = "PAYPALISHIRING", numRows = 4
# Выходные данные: "PINALSIGYAHRPI"
# Пояснение:
# P I N
# A L S I G
# Y A H R
# P I
# Пример 3:

# Входные данные: s = "A", numRows = 1
# Выходные данные: "A"
 

# Ограничения:

# 1 <= s.length <= 1000
# s состоит из английских букв (строчных и прописных), ',' и '.'.
# 1 <= numRows <= 1000







class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: single row or more rows than characters
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return ''.join(rows)