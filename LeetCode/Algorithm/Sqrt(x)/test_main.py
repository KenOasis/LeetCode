from math import sqrt
class Solution:
    def mySqrt(self, x: int) -> int:
        bound_1 = 1
        bound_2 = x
        mid = (bound_1 + bound_2 )// 2
        while abs(bound_1 - bound_2) // 2 >= 1:
            bound_2 = x // mid;
            bound_1 = mid
            mid = (bound_1 + bound_2)//2
        return int(mid)
def test_main():
    s =  Solution()
    for i in range(0, 1000000):
        assert sqrt(i)//1 == s.mySqrt(i)

test_main()
                