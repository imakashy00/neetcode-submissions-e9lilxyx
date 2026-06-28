class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = float('-inf')
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                maxP = max(prod, maxP)
        return maxP 