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

class RetweetDialog(WebComponent):
    def __init__(self):
        json_path = os.path.dirname(_components.__file__)
        super(RetweetDialog, self).__init__(self.__class__, json_path)

    def retweet(self, count):
        self.retweet_button.click()



