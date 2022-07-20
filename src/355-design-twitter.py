import heapq
from collections import defaultdict


class Twitter(object):

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # list of [count, tweetId]
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId):
        result = []
        maxHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                lastIndex = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][lastIndex]
                maxHeap.append([count, tweetId, followeeId, lastIndex - 1])
        heapq.heapify(maxHeap)

        while maxHeap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            result.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, index - 1])

        return result

    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
