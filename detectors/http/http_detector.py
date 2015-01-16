from detector import Detector
from math import sqrt

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime, timedelta


from alert import Alert, Base


class HTTPDetector(Detector):
    """docstring for HTTPDetector"""
    def __init__(self, checks=[], blacklistable=False, threshold=5, minimum_connections=6):
        super(HTTPDetector, self).__init__(checks)
        self.threshold = threshold
        self.minimum_connections = minimum_connections
        self.engine = create_engine('mysql://root:shiva@localhost/snort')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def check(self, alert):
        # grab previous connections from the database
        connections = self.get_last_connections(alert.origin_ip, alert.destination_ip)
        # only run the check if we've got enough connections to make the results sensible
	print len(connections)
        if len(connections) > self.minimum_connections:
            print "Checking, " + str(len(connections)) + " connections available"
            if isinstance(alert.timestamp, datetime):
                current_connection_time = alert.timestamp
            else:
                current_connection_time = datetime.strptime(alert.timestamp, "%Y-%m-%d %H:%M:%S")
            previous_connection_time = None
            time_delta_list = []
            #build timedeltas
            for conn in connections:
                previous_connection_time = conn.timestamp
                time_delta_list.append((previous_connection_time - current_connection_time).total_seconds())
                current_connection_time = conn.timestamp
            sorted_deltas = sorted(time_delta_list)
            list_size = len(sorted_deltas)
            # generate the subsets and check for matches
            difference = list_size - self.minimum_connections
            list_of_stdevs = []
            for i in xrange(difference + 1):
                list_of_stdevs.append(round((sorted_deltas[(self.minimum_connections + i - 1)] - sorted_deltas[i])/sqrt(2*list_size), 3))
            print list_of_stdevs
            positive_subsets = 0
            pos_subset_list = []
            for result in list_of_stdevs:
                if result < self.threshold: 
                    positive_subsets += 1
                    pos_subset_list.append(result)
            #if we've got matches, return them
            if positive_subsets > 0:
                return_string = "Suspected HTTP botnet connection, subset diffs:" + str(pos_subset_list)
                print return_string
                return return_string
            return False

    def get_last_connections(self, src, dest):
        session = self.Session()
        query = session.query(Alert).filter_by(origin_ip=src, destination_ip=dest)
        query_list = query.all()
        alert_list = []
	for alert in query_list:
	    if "http" in alert.alert_type:
	        alert_list.append(alert)
        print alert_list
        return alert_list
