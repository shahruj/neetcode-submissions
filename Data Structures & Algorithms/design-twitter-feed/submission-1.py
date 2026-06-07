import time

class Twitter:

    def __init__(self):
        self.posts = {}   # userId -> [(timestamp, counter, tweetId)]
        self.users = {}   # userId -> set of followees
        self.counter = 0  # ensures uniqueness

    def postTweet(self, userId: int, tweetId: int) -> None:
        ts = time.time()  # unix timestamp (float seconds)
        self.counter += 1

        if userId not in self.posts:
            self.posts[userId] = []

        # store (timestamp, counter, tweetId)
        self.posts[userId].append((ts, self.counter, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        posts = []

        # own posts
        posts.extend(self.posts.get(userId, []))

        # following posts
        for f in self.users.get(userId, set()):
            posts.extend(self.posts.get(f, []))

        # sort by timestamp DESC, then counter DESC
        posts.sort(key=lambda x: (x[0], x[1]), reverse=True)

        return [tweetId for _, _, tweetId in posts[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return  # ignore self-follow
        if followerId not in self.users:
            self.users[followerId] = set()
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].discard(followeeId)