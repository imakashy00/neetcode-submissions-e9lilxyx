class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res:list[int] = []
        for i in range(len(nums)):
            prod:int = 1
            for j in range(len(nums)):
                if j!=i:
                    prod*=nums[j]
            res.append(prod)
        return res