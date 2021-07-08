from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        if len(digits) == 0:
            return output
        translator = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
                      '7':'pqrs','8':'tuv','9': 'wxyz'}
        
        for digit in digits:
            if len(output) == 0:
                for letter in translator[digit]:
                    output.append(letter)
            else:
                temp = output.copy()
                output.clear()
                for front_part in temp:
                    for letter in translator[digit]:
                        li = [front_part, letter]
                        output.append(''.join(li))
        return output

s = Solution()
digits = '2'
print(s.letterCombinations(digits))