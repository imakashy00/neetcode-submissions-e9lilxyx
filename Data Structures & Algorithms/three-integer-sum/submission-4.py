class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res:list[list[int]] = []
        for i in range(len(nums)-2):
            j,k = i+1,len(nums)-1
            while j < k :
                if nums[i] + nums[j] + nums[k] == 0 and [nums[i],nums[j],nums[k]] not in res:
                    res.append([nums[i],nums[j],nums[k]])
                    k-=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else :
                    j+=1
        return res