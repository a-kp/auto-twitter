from auto_twitter._components.post_login_home.home_stream import HomeStream as HS


__author__ = 'anupama'


class HomeStream(object):
    def __init__(self):
        self.hs = None

    def load(self):
        self.hs = HS()

    def retweet(self, count):
        HomeStream.load(self)
        self.hs.retweet(int(count))


