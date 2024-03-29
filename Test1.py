﻿"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。
示例 1:
    输入: [2,2,1]
    输出: 1
示例 2:
    输入: [4,1,2,1,2]
    输出: 4
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    
    
        if len(nums) == 1:
            return nums[0]

        num = 0

        for temp in nums:
            num = num ^ temp

        return num


