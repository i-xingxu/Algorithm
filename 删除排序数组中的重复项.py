# coding=utf-8
from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        for j in range(1, len(nums)):

            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

        return nums[:i + 1]

        # count = len(nums)
        # i = 1
        # while i < count:
        #     if nums[i - 1] == nums[i]:
        #         nums.pop(i)
        #         count -= 1
        #     i += 1
        #
        # return nums


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums=[1,1,2]
s = Solution()
print(s.removeDuplicates(nums))
