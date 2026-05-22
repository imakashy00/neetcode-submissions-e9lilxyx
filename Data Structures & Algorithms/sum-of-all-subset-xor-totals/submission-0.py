class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(ind, sol):
            if ind == len(nums):
                xor = 0
                for num in sol:
                    xor^=num
                return xor
            with_el = backtrack(ind+1,sol)
            sol.append(nums[ind])
            without_el = backtrack(ind+1,sol)
            sol.pop()
            return with_el + without_el
        return backtrack(0,[])