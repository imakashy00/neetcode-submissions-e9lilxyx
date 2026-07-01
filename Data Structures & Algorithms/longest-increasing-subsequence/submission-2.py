class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        hmap = {}
        def dfs(pre_ind, cur_ind):
            if cur_ind == len(nums):
                return 0
            if (pre_ind, cur_ind) in hmap:
                return hmap[(pre_ind, cur_ind)] 
            not_inc = dfs(pre_ind, cur_ind + 1)
            inc = 0
            if pre_ind == -1 or nums[cur_ind] > nums[pre_ind]:
                inc = 1+ dfs(cur_ind, cur_ind + 1)
            hmap[(pre_ind, cur_ind)] = max(inc, not_inc)
            return hmap[(pre_ind, cur_ind)]
        return dfs(-1, 0)