class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet:int = 0
        # pos_speed_pair = [[p,s] for p,s in zip(position,speed)]
        pos_speed_pair = list(zip(position,speed))
        car_stack = []
        for p,s in sorted(pos_speed_pair)[::-1]:
           car_stack.append((target - p) / s)
           if len(car_stack) >=2 and car_stack[-1] <= car_stack[-2]:
            car_stack.pop()
        return len(car_stack)

