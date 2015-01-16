from helpers.helpers import Alert


class AlertFileParser(object):
    """docstring for AlertFileParser"""
    def __init__(self, filename):
        super(AlertFileParser, self).__init__()
        self.alert_file = open(filename, 'r')

    def get_alerts(self):
        alert_list = []
        for line in self.alert_file:
            #print line
            alert = Alert()
            alert.alert_from_json(line)
            #print alert
            alert_list.append(alert)
        return alert_list
