class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1 
        x*=sign

        li = list(str(x))
        li.reverse()
        num = 0
        for digit in li:
            num = num*10 + int(digit)
        answer = num*sign
        if answer < pow(-2,31) or answer > pow(2,31) - 1:
            return 0
        else:
            return answer

s = Solution()
x = 123
print(s.reverse(x))
    
        