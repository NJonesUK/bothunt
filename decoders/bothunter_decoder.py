from decoder import Decoder

class BotHunterDecoder(Decoder):
    def as_string(self, alert):
        return """BotHunter alert triggered. 
    Infected Host: {0}
    Command and Control Hosts: {1}
    Infector Hosts: {2}
    Observed Start Time: {3}""".format(str(alert.origin_ip),  str(alert.alert['candchosts']),  str(alert.alert['infectorhosts']),  str(alert.alert['obstime']))

    def as_compressed_info(self, alert):
        return str(alert)
