class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ind = 0
        for i, num in enumerate(nums):
            if i>max_ind:
                break
            max_ind = max(num+i, max_ind)
            print(max_ind)
            if max_ind >= len(nums)-1:
                return True
        return False

            