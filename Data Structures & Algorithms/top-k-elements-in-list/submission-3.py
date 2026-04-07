class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq:dict[int,int] = {}
        for num in nums:
            freq[num]=1+freq.get(num,0)
        arr:list[list] = [[] for _ in range(len(nums) + 1)]
        for num,fr in freq.items():
            arr[fr].append(num)
        res:list[int] = []
        for i in range(len(arr)-1,0,-1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res