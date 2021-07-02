from typing import List
class Solution:
    """
        This is a binary serach implemented:
        !!! Pls mimic every possible situation step by step
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        upper_bound = len(nums) - 1
        lower_bound = 0
        mid = (upper_bound + lower_bound)//2
        found = False
        insert_pos = 0
        while upper_bound >= lower_bound and (not found):
            if nums[mid] == target:
                found = True
                insert_pos = mid
            elif nums[mid] > target:
                upper_bound = mid - 1
                mid = (upper_bound + lower_bound)//2
            else:
                lower_bound = mid + 1
                mid = (upper_bound + lower_bound)//2
        else:
            if found:
                return insert_pos
            elif upper_bound < lower_bound:
                return mid + 1
            else:
                return mid - 1
s = Solution()
nums = [1,3,5,6]
target = 7
print(s.searchInsert(nums, target))