from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        flag = True
        while flag:
            try:
                nums.remove(val)
            except ValueError:
                flag = False
        return len(nums)