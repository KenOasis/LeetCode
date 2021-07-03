class Solution:
    def climbStairs(self, n: int) -> int:
        steps = []
        for index in range(1,46):
            if index == 1 or index == 2:
                step = index
                steps.append(step)
            else:
                step = steps[index - 2] + steps[index - 3]
                steps.append(step)
            if n == index:
                return steps[index - 1]

s = Solution()
for i in range(1,11):
    print(s.climbStairs(i))