#!/usr/bin/python

import argparse
import json

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from config import detectors, monitors, alert_handlers, decoders, generic_detectors, Session, whitelist, blacklist, callback_obj
from helpers.helpers import Alert
from helpers.whitelist import WhiteList
from helpers.static_blacklist import IPBlackList
from monitor.alertfileparser import AlertFileParser

import sched
import time
import datetime

class BotHunt(object):
    """Main application class, passed to monitors to provide callback functionality"""
    def __init__(self, detectors, generic_detectors, monitors):
        super(BotHunt, self).__init__()
        self.detectors = detectors
        self.generic_detectors = generic_detectors
        self.monitors = monitors
        self.wl = WhiteList(Session)
        self.bl = IPBlackList(Session)
        self.engine = create_engine('mysql://root:shiva@localhost/snort')
        self.Session = sessionmaker(bind=self.engine)

    def check(self, alert):
        results = []
        # check whitelist, if destination host is whitelisted then bomb out here
        if whitelist:
            if self.wl.check_whitelist(alert.destination_ip):
                return True
        #check the static IP blacklist, if it's on there bomb out now
        if blacklist:
            if self.bl.check(alert.destination_ip):
                return "Destination IP is blacklisted"
        # Pass through any generic detectors applied to all traffic, such as bogon filters or blacklists
        for detector in self.generic_detectors:
            results.append(self.generic_detectors[detector].check(alert))
        if alert.alert_type != "none":
            results.append(self.detectors[alert.alert_type].check(alert))
        return results

    def callback(self, alerts):
        print "Checking " + str(alerts)
        for alert in alerts:
            alert.result = bh.check(alert)
            if alert.result:
                for ah in alert_handlers:
                    alert_handlers[ah].alert(alert)

def run(sc, bh): 
    print datetime.datetime.now()
    session = bh.Session()
    alerts = bh.monitors["snort"].process()
    for alert in alerts:
        results = bh.check(alert)
        alert.result = results
        if isinstance(results, basestring):
            for ah in alert_handlers:
                alert_handlers[ah].alert(alert)
        elif isinstance(results, bool):
                print "Whitelisted"
        else:
            for result in results:
                if result:
                    for ah in alert_handlers:
                        alert_handlers[ah].alert(alert)
                    break
        alert.alert = json.dumps(alert.alert)
        alert.result = str(alert.result)
        session.add(alert)
    session.commit()
    sc.enter(2, 1, run, (sc, bh))

parser = argparse.ArgumentParser(description='Network-level botnet detection')
parser.add_argument('-t, --testfile', dest='testfile', help='File for reading test input from')
parser.add_argument('-m, --monitor', dest='monitorfile', help='specifies to watch a given file for alerts')
parser.add_argument('-r, --run', dest='run', action='store_const', const=True, default=False, help='run in normal mode using the config defined in config.py')
parser.add_argument('-c', '--check-config', dest='check_config', action='store_const', const=True, default=False, help='check configuration')

args = parser.parse_args()

bh = BotHunt(detectors, generic_detectors, monitors)
callback_obj.add_callback(bh.callback)

# Test mode - runs a set of predefined alerts from a file through the defined detectors
# then prints out detection stats for each alert in the file.

if args.testfile is not None:
    afp = AlertFileParser(args.testfile) 
    for alert in afp.get_alerts():
        alerted = False
        #print alert
        alert.result = bh.check(alert)
        print alert.result
        if not isinstance(alert.result, basestring):
            for result in alert.result:
                if result:
                    alerted = True
                    break
        else:
            if alert.result:
                alerted = True
        if alerted:
            print decoders[alert.alert_type].as_string(alert)


elif args.monitorfile is not None:
    path = '/home/nick/3yp/hg/src/monitor/'
    monitors["file"].add_watch(path, callback)
    #monitors['file'].start()
elif args.run:
    for monitor in bh.monitors:
        bh.monitors[monitor].start()
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, run, (s,bh))
    s.run()
elif args.check_config:
    print "Config OK"
else:
    print parser.print_help()
