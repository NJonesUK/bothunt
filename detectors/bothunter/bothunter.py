from detector import Detector

class BothunterDetector(Detector):
    """docstring for BothunterDetector"""
    def __init__(self, session, score_threshold=0.5, whitelist=[]):
        super(BothunterDetector, self).__init__([])
        self.session = session
        self.score_threshold = score_threshold
        self.whitelist = whitelist
        
    def check(self, alert):
        try:
            if alert.alert["score"] > self.score_threshold:
                    return "BotHunter Score over configured threshold of " + str(self.score_threshold)
            else:
                    return False
        except KeyError:
            return False