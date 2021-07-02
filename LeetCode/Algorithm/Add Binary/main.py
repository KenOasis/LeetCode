class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_list, b_list = list(a), list(b)
        result = ''
        digit_len = max(len(a),len(b))
        increment = 0
        for index_ in range(-1, -digit_len-1, -1):
            digit_a, digit_b = 0, 0
            if -index_ <= len(a):
                digit_a = int(a_list[index_])
            if -index_ <= len(b):
                digit_b = int(b_list[index_])
            if digit_a and digit_b and increment:
                new_digit = 1
            elif digit_a and digit_b:
                new_digit = 0
                increment = 1
            elif (digit_a or digit_b) and increment:
                new_digit = 0
                increment = 1
            elif digit_a or digit_b or increment:
                new_digit = 1
                increment = 0
            else:
                new_digit = 0
            result += str(new_digit)
        if increment:
            result += str(increment)
        return result[::-1]

s = Solution()
a = '1010'
b = '1011'
print(s.addBinary(a,b))
            