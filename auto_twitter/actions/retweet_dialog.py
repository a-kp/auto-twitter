import datetime

from auto_twitter._components.post_login_home.retweet_dialog import RetweetDialog as RD


__author__ = 'anupama'


class RetweetDialog(object):
    def __init__(self):
        self.rd = None

    def load(self):
        self.rd = RD()

    def retweet(self):
        RetweetDialog.load(self)
        self.rd.retweet()


