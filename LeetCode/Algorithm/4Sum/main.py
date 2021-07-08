from typing import List
import bisect
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.Ksum(sorted(nums), target, 4)

    def Ksum(self, nums, target, k: int) -> list:
        lnums, ans = len(nums), []
        if lnums < k:  # less entries that k. Returns empty
            return ans
        if lnums == k and sum(nums) == target:  # size iqual than k and sum iqual that target
            return [nums]   # returns what receive
        if sum(nums[:k]) > target:  # the lowest entries in nums is to high
            return ans      # returns empty
        if sum(nums[-k:]) < target:  # the biggest entries in nums is to low
            return ans      # retirns empty
        if k == 1:
            # use bisect to try to find target in nums
            idx = bisect.bisect_right(nums, target) - 1
            if nums[idx] == target:
                return [[nums[idx]]]
            return ans
        already = set()     # cache to avoid try what was already tried, and to avoid duplicate answer
        for i in range(lnums - 1):
            val = nums[i]
            if val in already:  # already tested
                continue
            already.add(val)
            res = self.Ksum(nums[i+1:], target - val, k-1)
            for t in res:
                if len(t) == k-1:
                    t.insert(0, val)
                    tup = tuple(t)
                    if tup not in already:  # answer already found
                        ans.append(t)
                    already.add(tup)
        return ans

s = Solution()
nums = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5]
target = 0
print(s.fourSum(nums,target))
           