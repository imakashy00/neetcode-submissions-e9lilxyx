class Solution:
    def findMin(self, nums: List[int]) -> int:
        time:int = nums[0]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                time=nums[i+1]
        return time