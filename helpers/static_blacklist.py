from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from config import Base

class IPBlackListEntry(Base):
	"""docstring for IPBlackListEntry"""
	__tablename__ = "ip_blacklist"
	ipbl_id = Column(Integer, primary_key=True)
	ip = Column(String(45))

	def __init__(self):
		super(IPBlackListEntry, self).__init__()


class IPBlackList(object):
	"""docstring for BlackList"""
	def __init__(self, session):
		super(IPBlackList, self).__init__()
		self.Session = session
		
	def check(self, ip):
	        session = self.Session()
                result = session.query(IPBlackListEntry).filter_by(ip=ip).count()
		if result > 0:
			return True
		else:
			return False
