from decoder import Decoder

class HTTPDecoder(Decoder):
    def as_string(self, alert):
        return """HTTP based alert triggered. 
    Origin: {0}
    Destination: {1}
    Alert: {2}
    Timestamp: {3}
    Data: {4}""".format(str(alert.origin_ip),  str(alert.destination_ip),  str(alert.result), str(alert.timestamp), str(alert.alert))

    def as_compressed_info(self, alert):
        return str(alert)
