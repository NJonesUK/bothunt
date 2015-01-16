import re

bh_regex = {}
bh_regex['score'] = re.compile("Score:: *(.*)")
bh_regex['infected_host'] = re.compile("Infected Target: *(.*)")
bh_regex['infectors'] = re.compile("Infector List: *(.*)")
bh_regex['egg_src_list'] = re.compile("Egg Source List: *(.*)")
bh_regex['candchosts'] = re.compile("C&C List: *(.*)")
bh_regex['peer_list'] = re.compile("Peer Coord. List: *(.*)")
bh_regex['resource_list'] = re.compile("Resource List: *(.*)")
bh_regex['obstime'] = re.compile("Observed Start: *(.*)")
bh_regex['endtime'] = re.compile("Report End: *(.*)")
bh_regex['gentime'] = re.compile("Gen. Time: *(.*)")

bh_text_dict = {}
bh_text_dict['score'] = re.compile("Score")
bh_text_dict['infected_host'] = re.compile("Infected Target")
bh_text_dict['infectors'] = re.compile("Infector List")
bh_text_dict['egg_src_list'] = re.compile("Egg Source List")
bh_text_dict['candchosts'] = re.compile("C&C List")
bh_text_dict['peer_list'] = re.compile("Peer Coord. List")
bh_text_dict['resource_list'] = re.compile("Resource List")
bh_text_dict['obstime'] = re.compile("Observed Start")
bh_text_dict['endtime'] = re.compile("Report End")
bh_text_dict['gentime'] = re.compile("Gen. Time")

bh_sep_regex = re.compile("=+ SEPARATOR =+")