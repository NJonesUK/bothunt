from alert_handler import AlertHandler

class PrintAlert(AlertHandler):
    def __init__(self, decoders):
        super(PrintAlert, self).__init__()
        self.decoders = decoders

    def alert(self, alert):
        print self.decoders[alert.alert_type].as_string(alert)
