class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq:dict[int,int] = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        arr:list[list[int]] = []
        for num,freq in freq.items():
            arr.append([freq,num])
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res