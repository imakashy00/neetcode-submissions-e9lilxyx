class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hset = set()
        for num in nums:
            if num not in hset:
                hset.add(num)
            else :
                return num