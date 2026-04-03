class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Works only with positive numbers

        # check:int = 0
        # for num in nums:
        #     mask:int = 1 << num 
        #     if check & 1<<num > 0:
        #         return True
        #     else:
        #         check = check | mask 
        # return False

        seen:set = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        