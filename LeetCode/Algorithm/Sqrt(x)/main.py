class Solution:
    def mySqrt(self, x: int) -> int:
        """
            Simply way but slow
        """
        step, sum = 1,1
        while x > sum:
            step += 2
            sum += step
        if sum == x:
            return step//2 + 1
        else:
            return step//2
class Solution2:
    """
        A solution like binary search, the speed is fastly a lot than the Simple Solution
    """
    def mySqrt(self, x: int) -> int:
        bound_1 = 1
        bound_2 = x
        mid = (bound_1 + bound_2 )// 2
        while abs(bound_1 - bound_2) // 2 >= 1:
            bound_2 = x // mid;
            bound_1 = mid
            mid = (bound_1 + bound_2)//2
        return int(mid)
s =  Solution()
for i in range(0, 20):
    print(s.mySqrt(i), end= ", ")
                