class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse = True) 
            heaviest = stones[0]
            sec_heaviest = stones[1]
            if heaviest == sec_heaviest:
                stones.remove(heaviest)
                stones.remove(sec_heaviest)
            else:
                stones[0] = heaviest - sec_heaviest
                stones.remove(sec_heaviest)
        return stones[0] if stones else 0