from detector import Detector
from rishi import Rishi
from command import IRCCommand
import json


class IRCAlertData(object):
    snort_rule = None
    data = None

    def __init__(self, snort_rule=None, data=None):
        self.snort_rule = snort_rule
        self.data = data

    def __repr__(self):
        return str(self.snort_rule) + ' : ' + str(self.data)

    def data_decode(self, dct):
        self.snort_rule = dct['snort_rule']
        self.data = dct['data']

    def data_from_json(self, alert_data):
        json.loads(alert_data)


class IRCDetector(Detector):
    def __init__(self):
        irc_checks = {}
        irc_checks['rishi'] = Rishi()
        irc_checks['irc command'] = IRCCommand()
        super(IRCDetector, self).__init__(irc_checks)
        self.irc_rules = {}
        self.irc_rules[12] = 'rishi'
        self.irc_rules[10] = 'irc command'

    def check(self, alert):
        detector = self.irc_rules[alert.alert["snort_rule"]]
        result = self.checks[detector].test(alert.alert["data"])
        return result
