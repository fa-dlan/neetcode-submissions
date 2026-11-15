class Twitter:

    def __init__(self):
        self.posts = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for post in self.posts[::-1]:
            if len(tweets) == 10:
                break
            if (post[0] == userId or 
                userId in self.follows and
                post[0] in self.follows[userId]
            ):
                tweets.append(post[1])
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set([followeeId])
        else:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return
        self.follows[followerId].discard(followeeId)