class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        
        if num >= 1000 and num < 4000:
            digit = num // 1000
            num -= (digit * 1000)
            while digit > 0:
                result += 'M'
                digit -= 1
            
        if num >= 100 and num < 1000:
            digit = num // 100
            num -= (digit * 100)
            if digit <= 3:
                while digit > 0:
                    result += 'C'
                    digit -= 1
            elif digit == 4:
                result += 'CD'
            elif digit >= 5 and digit <= 8:
                result += 'D'
                digit -= 5
                if digit <= 3:
                    while digit > 0:
                        result += 'C'
                        digit -= 1
            elif digit == 9:
                result += 'CM'

        if num >= 10 and num < 100:
            digit = num // 10
            num -= (digit*10)
            if digit <= 3:
               while digit > 0:
                   result += 'X'
                   digit -= 1
            elif digit == 4:
                result += 'XL'
            elif digit >= 5 and digit <= 8:
                result += 'L'
                digit -= 5
                if digit <= 3:
                    while digit > 0:
                        result += 'X'
                        digit -= 1
            elif digit == 9:
                result += 'XC'

        if num >= 1 and num < 10:
            digit = num
            if digit <= 3:
               while digit > 0:
                   result += 'I'
                   digit -= 1
            elif digit == 4:
                result += 'IV'
            elif digit >= 5 and digit <= 8:
                result += 'V'
                digit -= 5
                if digit <= 3:
                    while digit > 0:
                        result += 'I'
                        digit -= 1
            elif digit == 9:
                result += 'IX'

        return result

s = Solution()
num = 1994
print(s.intToRoman(num))