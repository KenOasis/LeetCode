from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        if len(nums) <= 1:
            return len(nums)
        for index in range(0, len(nums)):
            if nums[index] == nums[k]:
                continue
            else:
                k += 1
                nums[k] = nums[index]
        return k + 1

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = s.removeDuplicates(nums)
print(k, end = ', ')
print(nums)


