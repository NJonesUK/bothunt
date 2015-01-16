"""
IRC Detector Commands List

List of regular expressions 
"""

import re

regex_strings_list = []

#### DDOS Attacks ####
# agobot
regex_strings_list.append("ddos.stop")
regex_strings_list.append("ddos.phatwonk")
regex_strings_list.append("ddos.phatsyn")
regex_strings_list.append("ddos.phaticmp")
regex_strings_list.append("ddos.synflood")
regex_strings_list.append("ddos.updflood")
regex_strings_list.append("ddos.targa3")
regex_strings_list.append("ddos.httpflood")

# SDBot
regex_strings_list.append("syn") #(sdbot 05b pure version)
regex_strings_list.append("udp") #(sdbot 05b ago version)
regex_strings_list.append("ping")
# UrXbot
regex_strings_list.append("ddos.(syn|ack|random)")
regex_strings_list.append("(syn|synflood)")
regex_strings_list.append("(udp|udpflood|:u\\r)")
regex_strings_list.append("(tcp|tcpflood) (syn|ack|random)")
regex_strings_list.append("(ping|pingflood|p\\r)")
regex_strings_list.append("(icmpflood|icmp)")
regex_strings_list.append("ddos.stop")
regex_strings_list.append("synstop")
regex_strings_list.append("pingstop")
regex_strings_list.append("udpstop")

#### Spreading ####
# Agobot
regex_strings_list.append("scan.addnetrange")
regex_strings_list.append("scan.delnetrange")
regex_strings_list.append("scan.listnetranges")
regex_strings_list.append("scan.clearnetranges")
regex_strings_list.append("scan.resetnetranges")
regex_strings_list.append("scan.enable") # Any of (Anubis Bagle CPanel DCOM DCOM2 Doom DW Ethereal HTTP Locator LSASS NetBios Optix SQL UPNP WKS)
regex_strings_list.append("scan.disable") # As above
regex_strings_list.append("scan.startall")
regex_strings_list.append("scan.stopall")
regex_strings_list.append("scan.start")
regex_strings_list.append("scan.stop")
regex_strings_list.append("scan.stats")
regex_strings_list.append("scan.host")
# SDBot & UrXBot
regex_strings_list.append("(scanall|sa)")
regex_strings_list.append("(scanstats|stats)")
regex_strings_list.append("scandel") # can be one of webdav ntpass netbios dcom135 dcom445 dcom1025 dcom2 iis5ssl mssql beagle1 beagle2 mydoom lsass_445 lsass_139 optix upnp netdevil DameWare kuang2 sub7
regex_strings_list.append("scanstop")
regex_strings_list.append("(advscan|:asc)")

#### Downloading files from the internet ####
# Agobot
regex_strings_list.append("http.download")
regex_strings_list.append("http.execute")
regex_strings_list.append("http.update")
regex_strings_list.append("ftp.download")
regex_strings_list.append("ftp.execute")
regex_strings_list.append("ftp.update")
# SDBot & UrXBot
regex_strings_list.append("(update|up\\r)")
regex_strings_list.append("(download|dl\\r)")

#### Local file IO ####
# SDBot & UrXBot
regex_strings_list.append("(execute|e\\r)")
regex_strings_list.append("(findfile|ff\\r) filename")
regex_strings_list.append("(rename|mv\\r)")
regex_strings_list.append("findfilestopp")

#### Sending Spam ####
# Agobot
regex_strings_list.append("cvar.set spam_aol_channel")
regex_strings_list.append("cvar.set spam_aol_enabled")
regex_strings_list.append("cvar.set spam_maxthreads")
regex_strings_list.append("cvar.set spam_htmlemail")
regex_strings_list.append("cvar.set aolspam_maxthreads")
regex_strings_list.append("spam.setlist")
regex_strings_list.append("spam.settemplate")
regex_strings_list.append("spam.start")
regex_strings_list.append("spam.stop")
regex_strings_list.append("aolspam.setlist")
regex_strings_list.append("aolspam.settemplate")
regex_strings_list.append("aolspam.setuser")
regex_strings_list.append("aolspam.setpass")
regex_strings_list.append("aolspam.start")
regex_strings_list.append("aolspam.stop")
# UrXBot
regex_strings_list.append("email")

#### Sniffing ####
# Agobot
regex_strings_list.append("cvar.set sniffer_enabled")
regex_strings_list.append("cvar.set sniffer_channel")
regex_strings_list.append("sniffer.addstring")
regex_strings_list.append("sniffer.delstring")
# SDBot
regex_strings_list.append(".carnivore")

#### Cloning ####
#SDBot & UrXBot
regex_strings_list.append("(clone|c\\r)")
regex_strings_list.append("clonestop")
regex_strings_list.append("(c_raw|c_r\\r)")
regex_strings_list.append("(c_mode|c_m\\r)")
regex_strings_list.append("(c_nick|c_n\\r)")
regex_strings_list.append("(c_join|c_j\\r)")
regex_strings_list.append("(c_part|c_p\\r)")
regex_strings_list.append("(c_privmsg|c_pm\\r)")
regex_strings_list.append("(c_action|c_a\\r)")
regex_strings_list.append("sdbot")


regex_list = []

for regex_string in regex_strings_list:
    regex = re.compile(regex_string)
    regex_list.append(regex)
