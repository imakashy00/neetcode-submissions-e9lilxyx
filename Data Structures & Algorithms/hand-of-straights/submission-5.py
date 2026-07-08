class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort() # O(nlogn)
        count = {}
        for num in hand: # O(n)
            count[num] = 1+count.get(num,0)
        print(count)
        for num in hand: # O(n)
            if count[num]:
                for i in range(num,num+groupSize): # O(groupSize)
                    print(i)
                    if count.get(i,0) ==0:
                        return False
                    count[i] -=1
        return True