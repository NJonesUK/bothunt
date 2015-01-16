from detector import AlertTest
from command_regex import regex_list


class IRCCommand(AlertTest):
    def __init__(self):
        pass

    def test(self, input_string):
        junk, input_string = input_string.split(':', 1)
        for regex in regex_list:
            #print "checking " + input_string + " against " + str(regex.pattern)
            if regex.findall(input_string):
                return "IRC Command Match against " + str(regex.pattern)
        return False
