class Twitter:

    def __init__(self):
        self.followHashmap = defaultdict(set)
        self.tweetsHashmap = defaultdict(deque)
        self.currentTime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweetsHashmap and len(self.tweetsHashmap[userId]) >= 10:
            self.tweetsHashmap[userId].popleft()
        self.tweetsHashmap[userId].append((tweetId,self.currentTime))
        self.currentTime += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        getCurrUserPosts = list(self.tweetsHashmap[userId])
        getFollowedUserPosts = []
        for followee in self.followHashmap[userId]:
            getFollowedUserPosts.extend(list(self.tweetsHashmap[followee]))
        allPost = getCurrUserPosts + getFollowedUserPosts
        allPost.sort(key=lambda x:x[1],reverse=True)
        m = len(allPost)
        return [allPost[i][0] for i in range(min(m,10))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.followHashmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followHashmap[followerId]:
            self.followHashmap[followerId].remove(followeeId)
