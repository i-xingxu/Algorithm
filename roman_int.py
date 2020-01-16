# coding=utf-8
class Solution:
    def romanToInt(self, s: str) -> int:
        int_sum: int = 0
        for i in s:
            if i == 'I': int_sum += 1
            if i == 'V': int_sum += 5
            if i == 'X': int_sum += 10
            if i == 'L': int_sum += 50
            if i == 'C': int_sum += 100
            if i == 'D': int_sum += 500
            if i == 'M': int_sum += 1000

        if 'IV' in s: int_sum -= 2
        if 'IX' in s: int_sum -= 2
        if 'XL' in s: int_sum -= 20
        if 'XC' in s: int_sum -= 20
        if 'CD' in s: int_sum -= 200
        if 'CM' in s: int_sum -= 200
        return int_sum


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
