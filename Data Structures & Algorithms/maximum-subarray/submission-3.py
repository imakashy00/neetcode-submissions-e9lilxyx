class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        for i in range(len(nums)):
            local_sum = 0
            for j in range(i,len(nums)):
                local_sum += nums[j]
                max_sum = max(max_sum, local_sum)
        return max_sum 

