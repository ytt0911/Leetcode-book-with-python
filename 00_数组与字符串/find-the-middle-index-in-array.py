class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_sum = 0
        for i,num in enumerate(nums):
            if left_sum*2 + num == s :
                return i
            left_sum += num
        return -1