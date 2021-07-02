from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for digit in digits:
            num = num*10 + int(digit)
        num += 1
        a = list(str(num))
        a = [int(digit) for digit in a]
        return a

s = Solution()
digits = [1,2,3,4]
print(s.plusOne(digits))