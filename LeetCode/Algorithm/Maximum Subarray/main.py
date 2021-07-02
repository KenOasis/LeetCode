from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_end = 0
        for index in range(0, len(nums)):
            max_end += nums[index]
            if max_so_far < max_end:
                max_so_far = max_end
            if max_end < 0:
                max_end = 0
        return max_so_far    
s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))