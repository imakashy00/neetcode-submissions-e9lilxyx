class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed, max_speed = res =1, max(piles)
        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid_speed)
            if total <= h:
                res = mid_speed
                max_speed = mid_speed - 1
            else :
                min_speed = mid_speed + 1
        return res