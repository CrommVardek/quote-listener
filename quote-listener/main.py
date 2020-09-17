import praw

if __name__ == '__main__':

    reddit = praw.Reddit(client_id="my client id",
                     client_secret="my client secret",
                     user_agent="my user agent")

    while True:
        for comment in reddit.subreddit("all").stream.comments(skip_existing=True):
            print(comment)
            #todo
