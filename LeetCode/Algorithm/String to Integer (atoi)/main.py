class Solution:
    """
        requirement is keep changing (a lot of exception case)
    """
    def remove_leading_white_space(self, s:str):
        """
            for loop may not run at all, so 'eles' clause
            is not run too.
        """
        for index in range(0, len(s)):
            if s[index] != ' ':
                return s[index:]
        return 0
    def myAtoi(self, s: str) -> int:
        s = self.remove_leading_white_space(s)
        seq_start_index = 0
        # Get the sign of the number
        if s == 0:
            return 0
        if s[0].isdigit():
            sign = 1
        elif s[0] == '+' or s[0] == '-':
            seq_start_index = 1
            if s[0] == '+':
                sign = 1
            else:
                sign = -1
        else:
            return 0
        for index in range(seq_start_index + 1, len(s) + 1):
            if s[seq_start_index:index].isdigit() == False:
                seq_end_index = index - 1
                break
        else:
            seq_end_index = len(s)
        if seq_end_index == seq_start_index:
            return 0
        num = sign*int(s[seq_start_index:seq_end_index])
        if num < -pow(2,31):
            num = -pow(2,31)
        elif num > pow(2,31) - 1:
            num = pow(2,31) - 1
        return num
sobj = Solution()
s = ""
print(sobj.myAtoi(s))
        