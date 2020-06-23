# coding=utf-8
# 有效的括号
# 给定一组字符串，判断是否是成对的括号
# 使用栈来姐决，先进后出

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        mapping = {'{': '}', '[': ']', '(': ')', '#': ''} # 需要增加 # 的对应，否则一些异常情况会报错比如 ）（
        stack = ['#']  # 栈
        for c in s:
            if c in mapping:
                stack.append(c)
            elif mapping[stack.pop()] != c:
                return False
        return len(stack) == 1


s = Solution()
a = ')('
print(s.isValid(a))
