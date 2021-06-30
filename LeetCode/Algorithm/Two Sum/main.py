from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for index_a in range(0, length):
            for index_b in range(0, length):
                if nums[index_a] + nums[index_b] == target and index_a != index_b:
                    return [index_a, index_b]