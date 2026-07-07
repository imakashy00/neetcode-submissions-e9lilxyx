class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = max_ind = curr_ind = 0
        for i in range(len(nums)-1):
            max_ind = max(max_ind, i+nums[i])
            if i == curr_ind:
                steps += 1
                curr_ind = max_ind
                if curr_ind >= len(nums):
                    break
        return steps