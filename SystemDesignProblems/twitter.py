class Twitter:
    curTime = 1
    class Tweet:
        def __init__(self, userId, tweetId):
            self.userId = userId
            self.tweetId = tweetId
            self.timeStamp = Twitter.curTime
            Twitter.curTime += 1

    class User:
        def __init__(self, userId):
            self.userId = userId
            self.followers = {}
            self.followees = {}
            self.tweetCache = []

    def __init__(self):
        self.users = {}
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = self.Tweet(userId, tweetId)
        if userId not in self.users:
            self.users[userId] = self.User(userId)
        if userId not in self.tweets:
            self.tweets[userId] = [tweet]
        else:
            self.tweets[userId].insert(0,tweet)
        for key in self.users:
            user = self.users[key]
            usersFollowees = user.followees.keys()
            if userId in usersFollowees or key == userId:
                if len(user.tweetCache) >= 10:
                    user.tweetCache.pop(-1)
                user.tweetCache.insert(0, tweet)

    def updateUserCacheAfterFollow(self,userId, followeeId):
        tweetsFromFollowee = self.tweets.get(followeeId, [])
        currentFollowerCache = self.users[userId].tweetCache
        newCache = list(set(tweetsFromFollowee + currentFollowerCache))
        newCache.sort(key=lambda x: -1 * x.timeStamp)
        user = self.users[userId]
        user.tweetCache = newCache[0:10]
    
    def updateUserCacheAfterUnfollow(self, userId):
        userFollowees = self.users[userId].followees
        allTweetsByFollowees = []
        for followeeId in userFollowees:
            allTweetsByFollowees += self.tweets[followeeId]
        allTweetsByUsers = self.tweets.get(userId, [])
        allTweetsByFollowees += allTweetsByUsers
        currentTweetCache = self.users[userId].tweetCache
        newTweetCache = list(set(currentTweetCache + allTweetsByFollowees))
        newTweetCache.sort(key=lambda x: -1 * x.timeStamp)
        self.users[userId].tweetCache = newTweetCache[0:10]


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        user = self.users[userId]
        tweetCache = user.tweetCache
        newsFeed = []
        for tweet in tweetCache:
            newsFeed.append(tweet.tweetId)
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = self.User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = self.User(followeeId)
        followerUser = self.users[followerId]
        followeeeUser = self.users[followeeId]
        followerUser.followees[followeeId] = True
        followeeeUser.followers[followerId] = True
        self.updateUserCacheAfterFollow(followerId, followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followerUser = self.users[followerId]
        followeeUser = self.users[followeeId]
        tweetCache = followerUser.tweetCache
        newTweetCache = []
        for tweet in tweetCache:
            if tweet.userId != followeeId:
                newTweetCache.append(tweet)
        followerUser.tweetCache = newTweetCache
        if followeeId in followerUser.followees:
            followerUser.followees.pop(followeeId)
            followeeUser.followers.pop(followerId)
        self.updateUserCacheAfterUnfollow(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)