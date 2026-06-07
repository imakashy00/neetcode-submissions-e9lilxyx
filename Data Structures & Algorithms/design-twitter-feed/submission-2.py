import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = {}
        self.followMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        mheap = []
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                ind = len(self.tweetMap[followeeId]) - 1
                count,tweetId = self.tweetMap[followeeId][ind]
                mheap.append([count, tweetId, followeeId, ind - 1])
        heapq.heapify(mheap)
        while mheap and len(res) < 10:
            count, tweetId, followeeId, ind = heapq.heappop(mheap)
            res.append(tweetId)
            if ind >= 0:
                count, tweetId = self.tweetMap[followeeId][ind]
                heapq.heappush(mheap,[count, tweetId, followeeId, ind - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and  followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
