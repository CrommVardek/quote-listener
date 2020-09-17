import praw

sitename = "quotelistenerbot"

if __name__ == '__main__':

    reddit = praw.Reddit(site_name=sitename)

    while True:
        for comment in reddit.subreddit("all").stream.comments(skip_existing=True):
            print(comment)
            #todo
