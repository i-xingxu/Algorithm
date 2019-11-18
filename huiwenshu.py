# coding=utf-8

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        count = len(str_x)
        if count == 2 or x < 0:
            if str_x[0] == str_x[1]:
                return True
            else:
                return False
        elif count == 1:
            return True
        db_times = count // 2 + 1  # 对比次数
        m = 0
        n = count - 1
        for i in range(1, db_times):
            if str_x[m] == str_x[n]:
                m += 1
                n -= 1
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(1000030001))
