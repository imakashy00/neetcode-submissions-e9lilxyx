class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        hmap = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        def backtrack(i:int,sol:str):
            if i == len(digits):
                return res.append(sol)
            curr_digit = digits[i]
            for letter in hmap[curr_digit]:
                backtrack(i+1,sol+letter)
        backtrack(0,"")
        return res