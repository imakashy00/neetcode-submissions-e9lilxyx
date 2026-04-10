class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if len(nums) == 0:
            return 0
        res,longest = 1,1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                longest+=1
                print(nums[i],nums[i+1],'=',longest)
            elif nums[i] == nums[i+1]:
                continue
            else:
                res = max(res,longest)
                longest = 1
        return max(res,longest)
