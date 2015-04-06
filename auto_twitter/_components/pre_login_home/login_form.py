__author__ = 'anupama'
# Copyright 2014 Anupama Kattiparambil Prakasan
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from testatron import WebComponent
from auto_twitter import _components
import os


class LoginForm(WebComponent):
    def __init__(self):
        json_path = os.path.dirname(_components.__file__)
        super(LoginForm, self).__init__(self.__class__, json_path)

    def login(self, username, password, fail=False):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()
        if fail:
            #TODO have error messages loaded from json
            self.s2l.wait_until_page_contains("and password you entered did not match our records", 30)
            # self.component_loader.detect_element("login_error_message", make_visible=True)
            # self.objectify("login_error_message", self.component_loader.props)
            # print(str(self.login_error_message.__dict__))

# login = Login ("pre_login_home.json", "login-span")
# login.login("netsgr8_4us@yahoo.com" , "thisispassword")

