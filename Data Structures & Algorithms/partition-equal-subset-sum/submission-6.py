class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        hmap = {}
        def dfs(ind,cur_sum):
            if cur_sum == target :
                return True
            if ind == len(nums) or cur_sum > target:
                return False
            if (ind, cur_sum) in hmap:
                return hmap[(ind, cur_sum)]
            hmap[(ind, cur_sum)] = dfs(ind+1, cur_sum) or dfs(ind+1,cur_sum+nums[ind])
            return hmap[(ind, cur_sum)]
        return dfs(0,0)
