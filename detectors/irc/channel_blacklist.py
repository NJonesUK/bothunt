class ChannelBlacklist(object):
    """docstring for ChannelBlacklist"""
    def __init__(self, session):
        super(ChannelBlacklist, self).__init__()
        self.session = session

    def check_blacklist(self, alert):
        self.session.
        
class Data(Base):
    sid = Column(Integer, primary_key=True)
    cid = Column(Integer, primary_key=True)
    data_payload = Column(String, nullable=True)
    __tablename__ = 'data'
