import heapq

class Twitter:

    def __init__(self):
        self.posts = {}   # userId -> list of (time, tweetId)
        self.users = {}   # userId -> set of followees
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        # users to check (self + followees)
        followees = self.users.get(userId, set()) | {userId}

        for uid in followees:
            if uid in self.posts and self.posts[uid]:
                idx = len(self.posts[uid]) - 1
                time, tweetId = self.posts[uid][idx]
                # push latest tweet from each user
                heapq.heappush(heap, (-time, tweetId, uid, idx - 1))

        res = []
        while heap and len(res) < 10:
            time, tweetId, uid, idx = heapq.heappop(heap)
            res.append(tweetId)

            # push next tweet from same user
            if idx >= 0:
                t, tid = self.posts[uid][idx]
                heapq.heappush(heap, (-t, tid, uid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.users:
            self.users[followerId] = set()
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].discard(followeeId)