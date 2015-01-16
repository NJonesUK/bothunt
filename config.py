from callback import CallBack
callback_obj = CallBack()

#importing detectors
from detectors.irc.irc_detector import IRCDetector
from detectors.irc.rishi import Rishi
from detectors.http.http_detector import HTTPDetector
from detectors.bogon import BogonDetector

#importing alert handlers
from alert_handlers.email_alerts import EmailAlerts
from alert_handlers.print_alert import PrintAlert

#importing monitors
from monitor.snortmon import SnortMon

#importing decoders
from decoders.irc_decoder import IRCDecoder
from decoders.http_decoder  import HTTPDecoder

#database imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

#dictionaries to contain each module type. DO NOT ALTER
detectors = {}
generic_detectors = {}
monitors = {}
alert_handlers = {}
decoders = {}

#database definition
Base = declarative_base()
engine = create_engine('mysql://root:shiva@localhost/snort')
Session = sessionmaker(bind=engine)
session = Session()

#enable both whitelist and blacklist
whitelist = True
blacklist = True

#defining specific detectors
detectors["irc"] = IRCDetector()
detectors["http"] = HTTPDetector()

#defining generic detectors
generic_detectors["bogon"] = BogonDetector(session)

#defining decoders - note that these must match the detectors they go with
decoders["irc"] = IRCDecoder()
decoders["http"] = HTTPDecoder()

#define alert handlers
#email_alert = EmailAlerts(decoders, "localhost", "user", "pass", "none@none.com", "nick@nojones.net")
#alert_handlers["email"] = email_alert
alert_handlers["print"] = PrintAlert(decoders)

#define monitors
snort_monitor = SnortMon(waldo_file="waldo.txt")
irc_sigs = (6667,6668)
http_sigs = (2000002,)
icmp_sigs = (45477,)
snort_monitor.add_sigs("irc", irc_sigs)
snort_monitor.add_sigs("http", http_sigs)
snort_monitor.add_sigs("none", icmp_sigs)
monitors["snort"]  = snort_monitor
