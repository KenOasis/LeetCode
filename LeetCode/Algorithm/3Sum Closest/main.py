from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        nums.sort()
        for index in range(0, len(nums)):
            a = nums[index]
            start = index + 1
            end = len(nums) - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                sum1 = a + b + c
                if sum1 > target:
                    end -= 1
                else:
                    start += 1
                if abs(target - sum1) < abs(target - result):
                    result = sum1
        return result
