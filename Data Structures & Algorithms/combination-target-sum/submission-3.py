class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(ind,remain,sol):
            if remain == 0:
                return res.append(sol[:])
            if remain < 0 or ind == len(nums):
                return
            if nums[ind] <= remain:
                sol.append(nums[ind])
                backtrack(ind,remain-nums[ind],sol) # not ind+1 bcz reuseablility of num
                sol.pop()            
            backtrack(ind+1,remain,sol) #skipping the number
        backtrack(0,target,[])
        return res