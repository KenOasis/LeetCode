from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        front = 0
        end = len(height) - 1
        while front < end:
            """
                if the front line is shorter, we looking for a lower after it 
                since the distance is decreasing, it must be larger area if and only if have longer line; the same situation as the end line. Since we start at the two end of the lines, it gurantee the we get the max container at the end of iteration
                Also, if we have a long distance between two line which cause the larger area, it must include in our answer since we start from the two ends
            """
            if height[front] < height[end]:
                area = height[front] * (end - front)
                front += 1
            else:
                area = height[end] * (end - front)
                end -= 1
            if area > max_area:
                max_area = area
        return max_area

s = Solution()
height = [20,10,246,5]
print(s.maxArea(height))