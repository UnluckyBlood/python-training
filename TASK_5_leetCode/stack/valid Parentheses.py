# Valid Parentheses
# Easy
# Topics
# Company Tags
# Hints
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.



class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        sko = {")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if i in sko:
                if not stack or stack[-1] != sko[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack
sol = Solution()
s = "([{]})"
print (sol.isValid(s))



# самый быстрый 
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '[' 
        }

        stack = []
        for p in s:
            if p not in pairs:
                stack.append(p)
                continue
            
            if not stack or pairs[p] != stack.pop():
                return False
            
        return len(stack) == 0
# по сути без начальной проверки длины и первернута проверка
# в начале проверяем является ли ключём в словаре наш символ, если нет то добавляем в стэк, и скипаем следующие строчки в этом проходе
# вторая проверка если стек пуст, а мы встретили закрывающую скобку p, то для неё нет соответствующей открывающей скобки , а это ошибка
# pairs[p] != stack.pop()  делает сразу два дела, удаляет последний элемент списка stack, возвращает значение этого удалённого элемента
# pairs[p]  это ожидаемая открывающая скобка. Например если p ==")", то pairs[p] == '('
