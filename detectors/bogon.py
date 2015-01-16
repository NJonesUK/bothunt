from helpers.ip import addressInNetwork
from detector import Detector

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from alert import Alert, Base

class BogonDetector(Detector):
    """docstring for BogonDetector"""
    def __init__(self, session, checks=[], net_check=False, home_net="10.0.0.0/24"):
        super(BogonDetector, self).__init__(checks)
        self.session = session
        self.net_check = net_check
        self.home_net = home_net

    def check(self, alert):
        if alert.origin_ip is not None:
            ip = alert.origin_ip
            if self.net_check:
                if alert.destination_ip is not None:
                    if not (addressInNetwork(alert.origin_ip, self.home_net) or addressInNetwork(alert.destination_ip, self.home_net)):
                        return "Spoofed sender detected: " + ip
            bogons = self.session.query(Bogon).all()
            for bogon in bogons:
                if addressInNetwork(ip, bogon.ip_range):
                    return "Bogon spotted:" + ip + " in subnet " + bogon.ip_range
        return False

class Bogon(Base):
    """docstring for Bogon"""
    bogon_id = Column(Integer, primary_key=True)
    ip_range = Column(String(45))
    __tablename__ = "bogon"

    def __init__(self):
        super(Bogon, self).__init__()
        