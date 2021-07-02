class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_str = s.split(" ")
        for index_ in range(-1, -len(split_str)-1, -1):
            if split_str[index_] != "":
                return len(split_str[index_])
        else:
            return 0

s = Solution()
st = " a "
print(s.lengthOfLastWord(st))