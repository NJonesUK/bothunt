import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Alert(Base):
    alert_id = Column(Integer, primary_key=True)
    alert_type = Column(String)
    alert = Column(Text)
    timestamp = Column(DateTime)
    origin_ip = Column(String)
    destination_ip = Column(String)
    result = Column(Text)
    __tablename__ = "alert"

    def __repr__(self):
        return str(self.alert_type) + ' : ' + str(self.alert)

    # def alert_decode(self, dct):
    #     self.alert_type = dct['alert_type']
    #     self.alert = dct['alert']
    #     self.origin_ip = dct['src']
    #     self.destination_ip = dct['dest']

    # def alert_from_json(self, alert_json):
    #     json.loads(alert_json, object_hook=self.alert_decode)
