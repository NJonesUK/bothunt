import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql://root:shiva@localhost/snort')
Session = sessionmaker(bind=engine)
session = Session()

class Bogon(Base):
    """docstring for Bogon"""
    bogon_id = Column(Integer, primary_key=True)
    ip_range = Column(String(45))
    __tablename__ = "bogon"

    def __init__(self):
        super(Bogon, self).__init__()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        bogonfile = open(sys.argv[1], 'r')

        session.query(Bogon).delete()
        session.commit()

        for line in bogonfile:
            if line[0] is '#':
                continue
            else:
                bogon = Bogon()
                bogon.ip_range = line
                session.add(bogon)
        session.commit()
    else:
        print "currently scanning for:", session.query(Bogon).count(), "bogons"