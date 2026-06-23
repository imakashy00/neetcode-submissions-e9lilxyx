class Solution:
    def rob(self, nums: List[int]) -> int:
        hmap = {}
        def loot(ind):
            if ind >= len(nums):return 0
            if ind in hmap:return hmap[ind]
            hmap[ind] = max(nums[ind] + loot(ind+2), loot(ind+1))
            return hmap[ind]
        return loot(0)