from detector import Detector
from helpers.ip import address

class DomainBlacklistDetector(Detector):
	"""docstring for DomainBlacklistDetector"""
	def __init__(self, arg):
		super(DomainBlacklistDetector, self).__init__()		