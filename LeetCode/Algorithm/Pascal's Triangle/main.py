from typing import List
from math import comb
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [[comb(level_length - 1, index) for index in range(0,level_length)] for level_length in range(1,numRows + 1)]

s = Solution()
numRows = 2
print(s.generate(numRows))