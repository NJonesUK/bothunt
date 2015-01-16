from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from config import Base

class WhitelistEntry(Base):
	"""docstring for WhitelistEntry"""
	__tablename__ = "whitelist"
	whitelist_id = Column(Integer, primary_key=True)
	ip = Column(String(45))

	def __init__(self):
		super(WhitelistEntry, self).__init__()


class WhiteList(object):
	"""docstring for WhiteList"""
	def __init__(self, Session):
		super(WhiteList, self).__init__()
		self.Session = Session
		
	def check_whitelist(self, ip):
		session = self.Session()
                result = session.query(WhitelistEntry).filter_by(ip=ip).count()
		if result > 0:
			return True
		else:
			return False
