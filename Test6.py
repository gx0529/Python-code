
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        index = length // 2
        nums.sort()
        return nums[index]