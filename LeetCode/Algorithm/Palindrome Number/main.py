class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        original = x
        reverse = 0
        while x > 0:
            reverse = reverse*10 + x % 10
            x//=10
        if original == reverse:
            return True
        else:
            return False

s = Solution()
x = -123321
print(s.isPalindrome(x))