# coding=utf-8

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) < 2:  # 为空时返回空，只有一个字符串时返回第一个字符串
            if strs == []:
                return ''
            else:
                return strs[0]
        for s in range(len(strs[0])):
            for j in strs[1:]:
                if s < len(j) and strs[0][s] == j[s]:  # 判断的哥字符长度是否比剩余字符长度长，取出第一个字符串中的每个字符，与其他字符串的每个对应位置的字符对比，相同继续，不相同退出循环
                    continue
                else:
                    return strs[0][:s]
        return strs[0]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['aa', 'a']))
