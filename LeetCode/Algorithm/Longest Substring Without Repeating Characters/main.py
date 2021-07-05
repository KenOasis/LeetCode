class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            max_len = 1
        for start_index in range(0, len(s)):
            for end_index in range(start_index + 1, len(s)):
                if s[end_index] not in s[start_index:end_index]:
                    if end_index + 1 - start_index > max_len:
                        max_len = end_index + 1 - start_index
                else:
                    break
        return max_len

sobj = Solution()
s = 'pwwkew'
print(sobj.lengthOfLongestSubstring(s))
