from bh_regex import *
import sys
sys.path.append("../")
from alert import Alert

class BotHunterParser(object):
    """docstring for BotHunterParser"""
    def __init__(self, session, callback):
        super(BotHunterParser, self).__init__()
        self.session = session
        self.callback = callback
        self.parse_handling = {}
        self.parse_handling['score'] = self.score_handler
        self.parse_handling['infected_host'] = self.ih_handler
        self.parse_handling['infectors'] = self.infectors_handler
        self.parse_handling['egg_src_list'] = self.egg_handler
        self.parse_handling['candchosts'] = self.canc_handler
        self.parse_handling['peer_list'] = self.peer_handler
        self.parse_handling['resource_list'] = self.resource_handler
        self.parse_handling['obstime'] = self.obs_handler
        self.parse_handling['endtime'] = self.endtime_handler
        self.parse_handling['gentime'] = self.gen_handler

    def parse(self, input_data):
        return self.file_to_alert_list(input_data)

    def file_to_alert_list(self, input_data):
        print "Parser has been called"
        profile = open(input_data, 'r')
        alert = self.new_bothunter_alert()
        return_list = []
        separator_found = False
        for line in profile:
            if bh_sep_regex.match(line):
                separator_found = True
            for regex in bh_regex:
                res = bh_regex[regex].findall(line)
                if res:
                    if separator_found:
                        return_list.append(alert)
                        alert = self.new_bothunter_alert()
                        separator_found = False
                    self.parse_handling[regex](res[0], alert)
        if not (alert in return_list):
            return_list.append(alert)
        self.callback.callback(return_list)

    def new_bothunter_alert(self):
        alert = Alert()
        alert.alert_type = "bothunter"
        alert.alert = {}
        alert.origin_ip = None
        alert.destination_ip = None
        return alert

    def score_handler(self, value, alert):
        print "adding score"
        alert.alert['score'] = value

    def ih_handler(self, value, alert):
        alert.alert['infected_host'] = value

    def infectors_handler(self, value, alert):
        alert.alert['infectors'] = value

    def egg_handler(self, value, alert):
        alert.alert['egg_src_list'] = value

    def canc_handler(self, value, alert):
        alert.alert['candchosts'] = value

    def peer_handler(self, value, alert):
        alert.alert['peer_list'] = value

    def resource_handler(self, value, alert):
        alert.alert['resource_list'] = value

    def obs_handler(self, value, alert):
        alert.alert['obstime'] = value

    def endtime_handler(self, value, alert):
        alert.alert['endtime'] = value

    def gen_handler(self, value, alert):
        alert.alert['gentime'] = value
        alert.timestamp = value

if __name__ == "__main__":
    bh = BotHunterParser(None)
    res = bh.file_to_alert_list("../detectors/bothunter/bh_testfile.txt")
    print "\n\n", res
