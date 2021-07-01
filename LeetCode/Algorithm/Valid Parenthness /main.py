class Solution:
    """
        Must consider all the extreme case!!
    """
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        parenth_stack = []
        for index in range(0, len(s)):
            p = s[index]
            if p in ['(','[','{']:
                parenth_stack.append(p)
            else:
                if len(parenth_stack) == 0:
                    return False
                pop = parenth_stack.pop()
                if p == ')' and pop != '(':
                    return False
                elif p == ']' and pop != '[':
                    return False
                elif p == '}' and pop != '{':
                    return False
        else:
            if len(parenth_stack) != 0:
                return False
            else:
                return True
sol = Solution()
s = "(())[]"
print(sol.isValid(s))