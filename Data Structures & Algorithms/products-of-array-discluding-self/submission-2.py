class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre:list[int] =[]
        suff:list[int] = []
        prod = 1
        for i in range(len(nums)):
            pre.append(prod)
            prod=prod*nums[i]
        prod=1
        for i in range(len(nums)-1,-1,-1):
            suff.append(prod)
            prod=prod*nums[i]
        suff=suff[::-1]
        res:list[int]=[]
        for i in range(len(nums)):
            res.append(suff[i]*pre[i])
        return res

            