class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(ind,remain,sol):
            if remain == 0:
                return res.append(sol[:])
            if remain < 0 or ind == len(candidates):
                return 
            # Include the num
            sol.append(candidates[ind])
            backtrack(ind+1, remain - candidates[ind], sol)
            sol.pop()               
            # Exclude the num
            while ind+1 < len(candidates) and candidates[ind] == candidates[ind+1]:
                ind+=1
            backtrack(ind+1,remain,sol)
        backtrack(0,target,[])
        return res