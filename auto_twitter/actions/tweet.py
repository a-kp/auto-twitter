import datetime

from auto_twitter._components.post_login_home.tweet_box import TweetBox


__author__ = 'anupama'


class Tweet(object):
    def __init__(self):
        self.tweet_box = None

    def load(self):
        self.tweet_box = TweetBox()

    def tweet(self, tweet_message, with_time_stamp=False):
        Tweet.load(self)
        if with_time_stamp:
            tweet_message += '\n' + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        self.tweet_box.tweet(tweet_message)


# def tweet(test_input=None):
#     print "test_input : " + str(test_input)
#     Tweet().new_tweet(test_input["tweet_message"] +"\n" + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))
