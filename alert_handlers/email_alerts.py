# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

import alert_handler

class EmailAlerts(alert_handler.AlertHandler):
    def __init__(self, decoders, smtphost, user=None, password=None, sender=None, recipients=None):
        self.decoders = decoders
        self.smtphost = smtphost
        self.user = user
        self.password = password
        self.sender = sender
        self.recipients = recipients

    def alert(self, alert):
        # me == the sender's email address
        # you == the recipient's email address
        print self.decoders[alert.alert_type].as_string(alert)
        msg = MIMEText(self.decoders[alert.alert_type].as_string(alert))
        msg['Subject'] = "Alert from XBDF"
        msg['From'] = self.sender
        msg['To'] = self.recipients

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP(self.smtphost)
        s.sendmail(self.sender, self.recipients, msg.as_string())
        s.quit()