from auto_twitter._components.pre_login_home.login_form import LoginForm

__author__ = 'anupama'


class Login(object):
    def __init__(self):
        self.login_form = None
        self.home_page = "https://twitter.com"

    def load(self):
        print "login load"
        self.login_form = LoginForm()

    def login(self, username, password, fail=False):
        Login.load(self)
        self.login_form.login(username, password, fail)


# def login_test(username):
#     Login().login_test("netsgr8_4us@yahoo.com", "thisispassword")

