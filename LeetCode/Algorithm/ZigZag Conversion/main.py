class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        initial_gap = (numRows - 1) * 2
        num_digit_added = 0
        result = ''
        while num_digit_added < len(s):
            back_gap = 0
            start_pos = 0
            front_gap = initial_gap - back_gap
            while front_gap >= 0 and back_gap >= 0:
                if num_digit_added == len(s):
                    break
                if back_gap == 0:
                    for index in range(start_pos, len(s), front_gap):
                        result += s[index]
                        num_digit_added += 1
                        if num_digit_added == len(s):
                            break
                elif front_gap > 0 and back_gap > 0:
                    index = start_pos
                    current_gap = 0
                    while index < len(s):
                        result += s[index]
                        num_digit_added += 1
                        if current_gap == 0 or current_gap == back_gap:
                            current_gap = front_gap
                        else:
                            current_gap = back_gap
                        index += current_gap
                        if num_digit_added == len(s):
                            break
                else:
                    for index in range(start_pos, len(s), back_gap):
                        result += s[index]
                        num_digit_added += 1
                        if num_digit_added == len(s):
                            break
                front_gap -= 2
                back_gap += 2
                start_pos += 1
        return result

def test_main():
    soj = Solution()
    s = "A"
    numsRow = 1
    expect = "A"
    assert (soj.convert(s,numsRow)) == expect