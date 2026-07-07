class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        max_ind = 0
        i = 0
        while max_ind < len(nums)-1:
            if nums[i]+i >= max_ind+nums[max_ind]:
                max_ind = nums[i]+i
                steps+=1
            i+=1            
        return steps
                
