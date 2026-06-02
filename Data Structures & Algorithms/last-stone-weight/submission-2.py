import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            sec_heaviest = heapq.heappop(stones)
            if heaviest!=sec_heaviest:
                heapq.heappush(stones, heaviest - sec_heaviest)
        return -stones[0] if stones else 0