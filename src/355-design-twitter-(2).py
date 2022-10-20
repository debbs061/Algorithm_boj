import heapq
from typing import List
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.newsFeed = defaultdict(list)  # key: userId, value: list
        self.followList = defaultdict(set)  # key: userId, value: set
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.newsFeed[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        result = []
        self.followList[userId].add(userId)

        # get all feeds from followers
        for followerId in self.followList[userId]:
            allFeeds = self.newsFeed[followerId]

            for idx, (time, tweetId) in enumerate(allFeeds):
                feed.append([-time, tweetId])

        # retrieve feeds order by most recent
        heapq.heapify(feed)  # List[List[]] => [[time, tweetId]]
        cnt = 0
        while cnt < 10 and feed:
            result.append(heapq.heappop(feed)[1])
            cnt += 1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)

# ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","follow","follow","follow","follow","follow","follow","follow","follow","follow","follow","follow","follow","getNewsFeed","getNewsFeed","getNewsFeed","getNewsFeed","getNewsFeed"]
# [[],[1,6765],[5,671],[3,2868],[4,8148],[4,386],[3,6673],[3,7946],[3,1445],[4,4822],[1,3781],[4,9038],[1,9643],[3,5917],[2,8847],[1,3],[1,4],[4,2],[4,1],[3,2],[3,5],[3,1],[2,3],[2,1],[2,5],[5,1],[5,2],[1],[2],[3],[4],[5]]
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
