class Solution:
    def romanToInt(self, s: str) -> int:
        current_symbol_pos = 0
        s = list(s)
        s.reverse()
        result = 0
        skip = False
        for index_ in range(0, len(s)):
            if skip:
                skip = False
                continue
            if s[index_] == 'I':
                result += 1
            elif s[index_] == 'V' or s[index_] == 'X':
                if s[index_] == 'V':
                    result += 5
                else:
                    result += 10
                if index_ < len(s) - 1 and s[index_ + 1] == 'I':
                    result -= 1
                    skip = True
            elif s[index_] == 'L' or s[index_] == 'C':
                if s[index_] == 'L':
                    result += 50
                else:
                    result += 100
                if index_ < len(s) - 1 and s[index_ + 1] == 'X':
                    result -= 10
                    skip = True
            elif s[index_] == 'D' or s[index_] == 'M':
                if s[index_] == 'D':
                    result += 500
                else:
                    result += 1000
                if index_ < len(s) - 1 and s[index_ + 1] == 'C':
                    result -= 100
                    skip = True
        return result

solution = Solution()
s = 'LVIII'
print(solution.romanToInt(s))