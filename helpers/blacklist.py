from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from config import Base


class DynamicBlacklistEntry(Base):
    __tablename__ = 'blacklist'

    blacklist_id = Column(Integer, primary_key=True)
    ip = Column(String)
    time_added = Column(DateTime)
    occurances = Column(Integer)
    last_occurance = Column(DateTime)
    severity = Column(Integer)

    def __init__(self, ip):
        self.ip = ip
        self.time_added = datetime.now()
        self.occurances = 1
        self.last_occurance = datetime.now()
        self.severity = 0

    def __repr__(self):
        return "<Blacklist(IP:'%s', Added:'%s', Severity'%s')>" % (self.ip, self.time_added, self.severity)


class DynamicBlacklist(object):
    def __init__(self, session):
        self.session = session

    def blacklist(self, ip):
        bl_entry = self.session.query(DynamicBlacklistEntry).filter(DynamicBlacklistEntry.ip == ip)
        if bl_entry is None:
            new_bl_entry = DynamicBlacklistEntry(ip)
            new_bl_entry.save()
        else:
            bl_entry.occurances += 1
            bl_entry.last_occurance = datetime.now()
            bl_entry.save()

    def check_blacklist(self, ip):
        bl_entry = self.session.query(DynamicBlacklistEntry).filter(DynamicBlacklistEntry.ip == ip)
        if bl_entry is not None:
            return bl_entry.severity
        else:
            return False

    def increase_severity(self, ip):
        bl_entry = self.session.query(DynamicBlacklistEntry).filter(DynamicBlacklistEntry.ip == ip)
        if bl_entry:
            bl_entry.severity += 1
            bl_entry.save()
        else:
            return False
