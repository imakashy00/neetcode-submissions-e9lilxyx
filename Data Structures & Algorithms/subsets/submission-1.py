class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        def backtrack(i):
            if i == len(nums):
                return res.append(sol[:])
            backtrack(i+1) # calling without adding current element
            sol.append(nums[i]) # adding element to the solution
            backtrack(i+1) # calling with current element added
            sol.pop() #remove the element to other possibilities
        backtrack(0)
        return res
            