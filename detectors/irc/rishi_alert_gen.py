import re

exp_file = open("./rishi_exp.py", 'r')

regex = re.compile(r"^# [^\,]*")

for line in exp_file:
	if regex.findall(line):
		print line
		print regex.groups

#{"alert_type":"irc","alert":"RBOT|F|USA|XP-54143"}