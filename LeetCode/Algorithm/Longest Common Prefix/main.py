from typing import List
class Solution:
    """
        Need to think all the extreme case, eg: empty string(""), all string are same
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1 or len(strs[0]) == 0:
            return strs[0]
        for end_index in range(1, len(strs[0]) + 1):
            prefix = strs[0][:end_index]
            print('prefix: ', prefix)
            for string in strs:
                compare_count = 0
                if len(string) >= len(prefix):
                    if string.startswith(prefix):
                        compare_count += 1
                    else:
                        return strs[0][:end_index - 1]
                if compare_count == 0:
                    return strs[0][:end_index - 1]
        else:
            return prefix

s = Solution()
strs = ["flower","flower","flower","flower"]
print(s.longestCommonPrefix(strs))