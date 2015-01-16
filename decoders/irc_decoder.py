from decoder import Decoder

class IRCDecoder(Decoder):
    def as_string(self, alert):
        return """IRC based alert triggered. 
    Origin: {0}
    Destination: {1}
    Alert: {2}
    Data: {3}""".format(str(alert.origin_ip),  str(alert.destination_ip),  str(alert.result),  str(alert.alert['data']))

    def as_compressed_info(self, alert):
        return str(alert)
