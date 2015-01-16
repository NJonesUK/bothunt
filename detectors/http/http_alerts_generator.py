import sys
sys.path.append("../../")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime, timedelta
import random

from alert import Alert, Base

engine = create_engine('mysql://root:shiva@localhost/snort')
Session = sessionmaker(bind=engine)
session = Session()
time = datetime.now()

for x in xrange(1,15):
	alert = Alert()
	alert.alert_type = "http"
	alert.alert = "test alert"
	alert.timestamp = time + timedelta(0,((30 * x) + random.randint(-20, 20)))
	alert.origin_ip = "192.168.0.15"
	alert.destination_ip = "192.168.0.100"
	session.add(alert)
	session.commit()

query = session.query(Alert)

print query.count()
print query.all()