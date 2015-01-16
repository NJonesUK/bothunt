from helpers.helpers import Alert

class Detector(object):
    def __init__(self, checks):
        self.checks = checks

    def check(self, alert):
        results = {}
        if self.appropriate_alert_type(alert):
            for check in self.checks:
                results[str(check)] = check.check(alert.alert)
        return results

    def appropriate_alert_type(self, alert_data):
        if isinstance(alert_data, Alert):
            return True
        else:
            return False


class AlertTest(object):
    """docstring for Check"""
    def __init__(self, arg):
        super(Check, self).__init__()
        self.arg = arg

    def test(self, alert):
        return False
