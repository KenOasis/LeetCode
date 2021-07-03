from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
            Do not return anything, modify nums1 in-place instead.
            Not Finished: need to implemented merge sort solution
        """
        cur_pos_nums1, cur_pos_nums2,cur_sorted_pos = 0,0,0
        nums1_copy = nums1.copy()
        nums1.clear()
        if m == 0:
            nums1.append(nums2[cur_pos_nums2])
            cur_pos_nums2 += 1
            cur_sorted_pos += 1
        else:
            nums1.append(nums1_copy[cur_pos_nums1])
            cur_pos_nums1 += 1
            cur_sorted_pos += 1

        while cur_sorted_pos < m + n:
            while cur_pos_nums1 < m:
                pos = 0
                while nums1[pos] < nums1_copy[cur_pos_nums1]:
                    pos += 1
                    if pos == cur_sorted_pos:
                        break
                nums1.insert(pos, nums1_copy[cur_pos_nums1])
                cur_pos_nums1 += 1
                cur_sorted_pos += 1
            while cur_pos_nums2 < n:
                pos = 0
                while nums1[pos] < nums2[cur_pos_nums2]:
                    pos += 1
                    if pos == cur_sorted_pos:
                        break
                nums1.insert(pos, nums2[cur_pos_nums2])
                cur_pos_nums2 += 1
                cur_sorted_pos += 1

s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)
        
            
        