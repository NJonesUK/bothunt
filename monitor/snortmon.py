import sys
sys.path.append("..")
import socket
import struct
import time
import datetime

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from monitor import Monitor
from alert import Alert, Base


class SnortMon(Monitor):
    """docstring for SnortMon"""
    def __init__(self, signatures={}, waldo_file=""):
        super(SnortMon, self).__init__()
        self.signatures = signatures
        if waldo_file:
            self.waldo_file = waldo_file
            wfile = open(waldo_file, 'r')
            self.last_seen_event = wfile.readline()
            wfile.close()
            if self.last_seen_event == "":
                self.last_seen_event = None
            else:
                self.last_seen_event = datetime.strptime(self.last_seen_event, "%Y-%m-%d %H:%M:%S")

    def add_sigs(self, category, sig_list):
        for sig in sig_list:
            self.signatures[sig] = category

    def process(self):
        engine = create_engine('mysql://root:shiva@localhost/snort')
        Session = sessionmaker(bind=engine)
        session = Session()
        alerts = []
        latest = self.last_seen_event
        sigs = session.query(Signature).filter(Signature.sig_sid.in_(self.signatures.keys())).all()
        for sig in sigs:
            query = session.query(Event).filter(Event.signature==sig.sig_id)
            if self.last_seen_event:
                result = query.filter(Event.timestamp > self.last_seen_event).all()
            else:
                result = query.all()
            for item in result:
                alert = Alert()
                alert.alert_type = self.signatures[sig.sig_sid]
                alert.alert = {}
                res_data = session.query(Data).filter(Data.cid==item.cid).filter(Data.sid==item.sid).all()
                alert.alert['data'] = res_data[0].data_payload.decode("hex")
                alert.alert['snort_rule'] = item.signature
                alert.result = None
                alert.timestamp = item.timestamp
                res_iphdr = session.query(Iphdr).filter(Iphdr.cid==item.cid).filter(Iphdr.sid==item.sid).all()
                alert.origin_ip = socket.inet_ntoa(struct.pack(">L", res_iphdr[0].ip_src))
                alert.destination_ip = socket.inet_ntoa(struct.pack(">L", res_iphdr[0].ip_dst))
                alerts.append(alert)
                print "New alert:" + str(alert)
                if latest is not None:
                    if item.timestamp > latest:
                        latest = item.timestamp
                else:
                    latest = item.timestamp
        session.close()
        self.last_seen_event = latest
        if self.waldo_file:
            wfile = open(self.waldo_file, 'w')
            wfile.write(datetime.strftime(self.last_seen_event, "%Y-%m-%d %H:%M:%S"))
            wfile.close()
        return alerts

class Data(Base):
    sid = Column(Integer, primary_key=True)
    cid = Column(Integer, ForeignKey("Event.cid"), primary_key=True)
    data_payload = Column(String, nullable=True)
    __tablename__ = 'data'

class Detail(Base):
    detail_type = Column(Integer, primary_key=True)
    detail_text = Column(String)
    __tablename__ = 'detail'

class Encoding(Base):
    encoding_type = Column(Integer, primary_key=True)
    encoding_text = Column(String)
    __tablename__ = 'encoding'

class Event(Base):
    sid = Column(Integer, primary_key=True)
    cid = Column(Integer, primary_key=True)
    signature = Column(Integer)
    timestamp = Column(DateTime)
    __tablename__ = 'event'

class Icmphdr(Base):
    sid = Column(Integer, primary_key=True)
    cid = Column(Integer, ForeignKey("Event.cid"), primary_key=True)
    icmp_type = Column(Integer)
    icmp_code = Column(Integer)
    icmp_csum = Column(Integer, nullable=True)
    icmp_id = Column(Integer, nullable=True)
    icmp_seq = Column(Integer, nullable=True)
    __tablename__ = 'icmphdr'

class Iphdr(Base):
    sid = Column(Integer, primary_key=True)
    cid = Column(Integer, ForeignKey("Event.cid"), primary_key=True)
    ip_src = Column(Integer)
    ip_dst = Column(Integer)
    ip_ver = Column(Integer, nullable=True)
    ip_hlen = Column(Integer, nullable=True)
    ip_tos = Column(Integer, nullable=True)
    ip_len = Column(Integer, nullable=True)
    ip_id = Column(Integer, nullable=True)
    ip_flags = Column(Integer, nullable=True)
    ip_off = Column(Integer, nullable=True)
    ip_ttl = Column(Integer, nullable=True)
    ip_proto = Column(Integer)
    ip_csum = Column(Integer, nullable=True)
    __tablename__ = 'iphdr'

class Opt(Base):
    sid = Column(Integer, primary_key=True)
    cid = Column(Integer, primary_key=True)
    optid = Column(Integer, primary_key=True)
    opt_proto = Column(Integer)
    opt_code = Column(Integer)
    opt_len = Column(Integer, nullable=True)
    opt_data = Column(String, nullable=True)
    __tablename__ = 'opt'

class Reference(Base):
    ref_id = Column(Integer, primary_key=True)
    ref_system_id = Column(Integer)
    ref_tag = Column(String)
    __tablename__ = 'reference'

class ReferenceSystem(Base):
    ref_system_id = Column(Integer, primary_key=True)
    ref_system_name = Column(String(60), nullable=True)
    __tablename__ = 'reference_system'

class Schema(Base):
    vseq = Column(Integer, primary_key=True)
    ctime = Column(DateTime)
    __tablename__ = 'schema'

class Sensor(Base):
    sid = Column(Integer, primary_key=True)
    hostname = Column(String, nullable=True)
    interface = Column(String, nullable=True)
    filter = Column(String, nullable=True)
    detail = Column(Integer, nullable=True)
    encoding = Column(Integer, nullable=True)
    last_cid = Column(Integer)
    __tablename__ = 'sensor'

class SigClass(Base):
    sig_class_id = Column(Integer, primary_key=True)
    sig_class_name = Column(String(180))
    __tablename__ = 'sig_class'

class SigReference(Base):
    sig_id = Column(Integer, primary_key=True)
    ref_seq = Column(Integer, primary_key=True)
    ref_id = Column(Integer)
    __tablename__ = 'sig_reference'

class Signature(Base):
    sig_id = Column(Integer, primary_key=True)
    sig_name = Column(String(765))
    sig_class_id = Column(Integer)
    sig_priority = Column(Integer, nullable=True)
    sig_rev = Column(Integer, nullable=True)
    sig_sid = Column(Integer, nullable=True)
    sig_gid = Column(Integer, nullable=True)
    __tablename__ = 'signature'

class Tcphdr(Base):
    sid = Column(Integer, primary_key=True)
    cid = Column(Integer, ForeignKey("Event.cid"), primary_key=True)
    tcp_sport = Column(Integer)
    tcp_dport = Column(Integer)
    tcp_seq = Column(Integer, nullable=True)
    tcp_ack = Column(Integer, nullable=True)
    tcp_off = Column(Integer, nullable=True)
    tcp_res = Column(Integer, nullable=True)
    tcp_flags = Column(Integer)
    tcp_win = Column(Integer, nullable=True)
    tcp_csum = Column(Integer, nullable=True)
    tcp_urp = Column(Integer, nullable=True)
    __tablename__ = 'tcphdr'

class Udphdr(Base):
    sid = Column(Integer, primary_key=True)
    cid = Column(Integer, ForeignKey("Event.cid"), primary_key=True)
    udp_sport = Column(Integer)
    udp_dport = Column(Integer)
    udp_len = Column(Integer, nullable=True)
    udp_csum = Column(Integer, nullable=True)
    __tablename__ = 'udphdr'

if __name__ == "__main__":
    irc_sigs = (6667,6668)
    http_sigs = (2000002,)
    sigs_to_monitor = {}
    for sig in irc_sigs:
        sigs_to_monitor[sig] = "IRC"
    for sig in http_sigs:
        sigs_to_monitor[sig] = "HTTP"

    engine = create_engine('mysql://root:shiva@localhost/snort')
    Session = sessionmaker(bind=engine)
    session = Session()
    sigs = session.query(Signature).filter(Signature.sig_sid.in_(sigs_to_monitor.keys())).all()
    for sig in sigs:
        result = session.query(Event).filter(Event.signature==sig.sig_id).all()
        for item in result:
            alert = Alert()
            alert.alert_type = sigs_to_monitor[sig.sig_sid]
            alert.alert = {}
            res_data = session.query(Data).filter(Data.cid==item.cid).filter(Data.sid==item.sid).all()
            alert.alert['data'] = res_data[0].data_payload.decode("hex")
            alert.alert['snort_rule'] = 12
            alert.result = None
            alert.timestamp = item.timestamp
            res_iphdr = session.query(Iphdr).filter(Iphdr.cid==item.cid).filter(Iphdr.sid==item.sid).all()
            alert.origin_ip = socket.inet_ntoa(struct.pack(">L", res_iphdr[0].ip_src))
            alert.destination_ip = socket.inet_ntoa(struct.pack(">L", res_iphdr[0].ip_dst))
