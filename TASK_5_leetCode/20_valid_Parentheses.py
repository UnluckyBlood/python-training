class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brack = {'(', '{', '['}
        matche = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for el in s:
            if el in open_brack:
                stack.append(el)
                print(stack)
            else:
                if not stack:
                    print (stack)
                    return False
                elif stack[-1] != matche[el]:
                    print(stack)
                    return False
                print(stack)
                stack.pop()
        print (stack)
        return len(stack) == 0
        

    
sol = Solution()
result = sol.isValid("{[()]}")
print(result)