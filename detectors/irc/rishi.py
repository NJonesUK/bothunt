from detector import AlertTest

import rishi_exp

import re

class Rishi(AlertTest):
    def __init__(self):
        self.regex_dict = self.init_exps()

    def test(self, input_string):
    	#junk, input_string = input_string.split(':', 1)
#        if "NICK" in input_string:
#            input_string = input_string[5:]
        for regex in self.regex_dict:
            if self.regex_dict[regex].findall(input_string):
                return "Rishi Nickname Match"
        return False

    def init_exps(self):
        regex_dict = {}
        for regex in rishi_exp.regexlist:
            compiled_regex = re.compile(regex, re.IGNORECASE)
            regex_dict[regex] = compiled_regex
        return regex_dict

    def __str__(self):
        return "Rishi IRC Nickname Detector"
