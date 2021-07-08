from typing import List
from math import comb
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex, index) for index in range(0,rowIndex + 1)]

s = Solution()
numRows = 0
print(s.generate(numRows))