"""Regular Expressions taken from the Rishi project, for identifying botnet IRC nicknames"""

regexlist = []
# AB|1234, ABCD||1234567
regexlist.append(r"[a-z]+\|+[0-9]{4,}")
# [0|1234], [1||1234567]
regexlist.append(r"\[[0-9]\|+[0-9]{4,}\]")
# [0]-1234, [1]-1234567, {0}-12345
regexlist.append(r"(\[|\{)[0-9](\]|\})-[0-9]{4,}")
# [AB|DEU|1234], [AB1234|USA|1234567]
regexlist.append(r"\[[a-z]+[0-9]*\|(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|[0-9]+\]")
# ruby1234
regexlist.append(r"ruby[0-9]+")
# A-1234, B-1234567, X1234
regexlist.append(r"[a-z]-?[0-9]{4,}")
# [AB]|1234, [ABCD]-1234567
regexlist.append(r"\[[a-z]+\](\||-)[0-9]{4,}")
# [RAPEDv12]-1234, [RAPEDv1234]-1234567
regexlist.append(r"\[RAPEDv[0-9]+\]-?[0-9]{4,}")
# ZOMBIE1234
regexlist.append(r"ZOMBIE[0-9]{4,}")
# |1234
regexlist.append(r"\|[0-9]{4,}")
# [A]1234, [ABCD]1234567
regexlist.append(r"\[[a-z]+\][0-9]{4,}")
# W0*1234
regexlist.append(r"W0.[0-9]{4,}")
# AB-|-1234, ABCD-|-1234567
regexlist.append(r"[a-z]{1,4}-\|-[0-9]{4,}")
# [A]ABCD|1234, [A]ABCD-1234
regexlist.append(r"\[[a-z]\][a-z]+(\||-)[0-9]{4,}")
# [ABC-1234]-12345
regexlist.append(r"\[[a-z]+-[0-9]+\]-[0-9]{4,}")
# |ABCD|A|1234
regexlist.append(r"\|[a-z]+\|[a-z]\|[0-9]{4,}")
# [1]|1234
regexlist.append(r"\[[0-9]\]\|[0-9]{4,}")
# |12|ABCD|1234
regexlist.append(r"\|[0-9]{1,2}\|[a-z]{1,4}\|[0-9]{4,}")
# [A][ABC]1234, [A][ABC]-1234
regexlist.append(r"\[[a-z]\]\[[a-z]+\]-?[0-9]{4,}")
# [ABCD][ABCD12-1234]
regexlist.append(r"\[[a-z]+\]\[[a-z0-9]+-[0-9]{4,}\]")
# |12||-X-||1234, |AB||-X-||1234
regexlist.append(r"\|[0-9|a-z]+\|\|-[a-z]-\|\|[0-9]{4,}")
# [ABCD-1234]
regexlist.append(r"\[[a-z]+-[0-9]{4,}\]") 
# [ABCD123]-1234
regexlist.append(r"\[[a-z0-9]+\]-[0-9]{4,}")
# [ABCD0374]1234
regexlist.append(r"\[([a-z]+[0,1,3,7,4]+)*\][0-9]{4,}")
# [AB||1234]
regexlist.append(r"\[[a-z0,1,3,7,4]+\|\|[0-9]{4,}\]")
# DEU|XP|SP4|496015
regexlist.append(r"(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|(XP|2K|K3|UN)\|[a-z0-9]{1,3}\|[0-9]{4,}")
# [999379|0|UUU]
regexlist.append(r"\[[0-9]{4,}\|[0-9]\|[a-z]{1,3}\]")
# [_]|309597
regexlist.append(r"\[.\]\|[0-9]{4,}")
# [[Xx0x0xX]]-803400, [|x00x|]96695
regexlist.append(r"\[[\[|\|][a-z,1,0,3,7,4]{1,9}[\]|\|]\]-?[0-9]{4,}")
# [19]le[XP]70736
regexlist.append(r"\[[0-9]{1,2}\][a-z]{1,2}\[[a-z]{1,2}\][0-9]{4,}")
# AB-1234
regexlist.append(r"[a-z]{1,2}-[0-9]{4,}")
# |00||DnB||2727
regexlist.append(r"\|[0-9]{1,2}\|{1,2}[a-z]{1,4}\|{1,2}[0-9]{4,}")
# FIRE_BOT_32306
regexlist.append(r"FIRE_BOT_[0-9]{4,}")
# Ayu-San|8034002
regexlist.append(r"[a-z]{1,3}-[a-z]{1,3}\|[0-9]{4,}")
# [R||184824682]
regexlist.append(r"\[.{1,2}\|\|[0-9]{4,}\]")
# {[52785]}
regexlist.append(r"\{\[[0-9]{4,}\]\}")
# br_pHeHIwc
regexlist.append(r"br_[a-z]{4,}")
# [I]jhrowfqkyrzf
regexlist.append(r"\[I\][a-z]{6,}")
# |LSD|-8238
regexlist.append(r"\|LSD\|\-[0-9]{4,}")
# r00t-R00T3D-9108
regexlist.append(r"r00t-[a-z0-9]{2,8}-[0-9]{4,}")
# cX-allmp3s-CD7671
regexlist.append(r"cX-all[a-z0-9]{1,6}-CD[0-9]{4,}")
# [M00|BGR|14086]
regexlist.append(r"\[[a-z][0-9]{1,2}\|[a-z]{1,3}\|[0-9]{4,}\]")
# [00|FRA|432865] [00|DEU|597660] [03|USA|147700] [00|KOR|437247]
regexlist.append(r"\[[0-9]{1,2}\|(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|[0-9]{4,}\]")
# URXv2-75863
regexlist.append(r"URXv[0-9]-[0-9]{4,}")
# xXx-803400248
regexlist.append(r"xXx-[0-9]{4,}")
# [-UrX-]-8034002
regexlist.append(r"\[-[a-z]{1,3}-\]-[0-9]{4,}")
# {RX}-527853
regexlist.append(r"\{[a-z]{1,3}\}-[0-9]{4,}")
# (&#O##@wGoacNEQ
regexlist.append(r"\(&.{4,}@[a-z]{4,}")
# kYprPp   FALSE-POSITIVE???
regexlist.append(r"\[a-z]{5,}")
# [CHN][0H]dcjsoywzo new[CHN][28H]dcjsoywzo
regexlist.append(r"(new|NE)?\[(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\]\[[0-9]{1,4}H\][a-z]{4,}")
# r00t3d-6485006232
regexlist.append(r"r00t3d-[0-9]{4,}")
# RBOT|F|USA|XP-11348
regexlist.append(r"RBOT\|[a-z]?\|?(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|(XP|2K|K3|UN)-[0-9]{4,}")
# RBOT||XP-SP2-80340024
regexlist.append(r"RBOT\|\|(XP|2K|K3|UN)-(SP2|SP4)-[0-9]{4,}")
# XP|00|DEU|1425
regexlist.append(r"(XP|2K|K3|UN)\|[0-9]{1,2}\|(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|[0-9]{4,}")
# roda69_1711
regexlist.append(r"roda[0-9]{1,2}_[0-9]{4,}")
# [FirstTime|00|SAU|XP|SP2]-49
regexlist.append(r"\[FirstTime\|[0-9]{1,2}\|(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|(XP|2K|K3|UN)\|SP[0-9]\]-[0-9]{2,}")
# UM114EC555267
regexlist.append(r"UM114EC[0-9]{4,}")
# p|iubfqr
regexlist.append(r"p\|[a-z]{4,}")
# What--2622
regexlist.append(r"What--[0-9]{4,}")
# [00|DEU|XP|SP2]-6820
regexlist.append(r"\[[0-9]{1,2}\|(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|(XP|2K|K3|UN)\|SP[0-9]\]-[0-9]{4,}")
# DEU|XP|SP2|00|1000|L|293
regexlist.append(r"(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|(XP|2K|K3|UN)\|SP[0-9]\|[0-9]{1,2}\|[0-9]{1,4}\|L\|[0-9]{1,3}")
# [XP|L|RUS|GRC|00]-tgQSTdLQ
regexlist.append(r"\[(XP|2K|K3|UN)\|L\|(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|[0-9]{1,2}\]-[a-z]{4,}")
# [DEU][3]11G-BL
regexlist.append(r"\[(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\]\[[0-9]{1,1}\][0-9]{1,2}[a-z]-[a-z]{2,}")
# [THA-[20H]tcpxhhcci
regexlist.append(r"\[(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)-\[[0-9]{1,2}H\][a-z]{4,}")
# \00\USA\jbmzb6upnw
regexlist.append(r"\\[0-9]{1,2}\\(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\\[a-z,0-9]{4,}")
# DEU|XP|LAN|9|838810041
regexlist.append(r"(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|(XP|2K|K3|UN)\|LAN\|[0-9]\|[0-9]{4,}")
# \00M\CHN\k6dj1myhia
regexlist.append(r"\\\d{1,2}[a-z]{1,2}?\\(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\\\w{4,}")
# [M|11|DEU|XP|34037]
regexlist.append(r"\[[a-z]\|[0-9]{1,2}\|(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|(XP|2K|K3|UN)\|[0-9]{3,}\]")
# [M00|THA|59007878]
regexlist.append(r"\[[a-z][0-9]{1,2}\|(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|[0-9]{4,}\]")
# ][l4m3r][gqaowo
regexlist.append(r"\]\[l4m3r\]\[[a-z]{4,}")
# NY8463404018863
regexlist.append(r"NY[0-9]{7,}")
# awk-7262056
regexlist.append(r"awk-[0-9]{4,}")
# T80-166013755
regexlist.append(r"T80-[0-9]{4,}")
# [XP|DEU]123456789
regexlist.append(r"\[(XP|2K|K3|UN)\|(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\]{4,}")
# ]tG[-xwakwp
regexlist.append(r"\]tG\[-[a-z]{4,}")
# [DEU-0H-ferwwgwq FQ[FRA-1H-sadfgww
regexlist.append(r"[a-z]{0,2}\[(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\-[0-9]H\-[a-z]{4,}")
# [DEU][12]91G-BW
regexlist.append(r"\[(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\]\[[0-9]{1,2}\]\w{1,3}\-[a-z]{1,2}")
# USA|XP|SP2|00|2341
regexlist.append(r"(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|(XP|2K|K3|UN)\|SP[0-9]\|[0-9]{1,2}\|[0-9]{3,}")
# [A][T][L]-3985100
regexlist.append(r"\[A\]\[T\]\[L\]-[0-9]{4,}")
# ][laMer][xdqikq
regexlist.append(r"\]\[laMer\]\[[a-z]{4,}")
# NT51|4357583
regexlist.append(r"NT[0-9]{1,2}\|[0-9]{4,}")
# [00][XP][SP2][USA]-751625146
regexlist.append(r"\[[0-9]{1,2}\]\[(XP|2K|K3|UN)\]\[SP[0-9]\]\[(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\]\-[0-9]{4,}")
# USA|00|XP|SP2|381
regexlist.append(r"(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|[0-9]{1,2}\|(XP|2K|K3|UN)\|SP[0-9]\|[0-9]{3,}")
# [USA|XP|L|00]-mmgjr
regexlist.append(r"\[(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|(XP|2K|K3|UN)\|[a-z]\|[0-9]{1,2}\]\-[a-z]{4,}")
# [LZ]WmLcbbFd
regexlist.append(r"\[LZ\][a-z]{4,}")
# bot-4184076-13
regexlist.append(r"bot-[0-9]{4,}-13")
# [nLh]DEU-265560
regexlist.append(r"\[nLh\](DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)-[0-9]{4,}")
# [MT01|LBN|80686]
regexlist.append(r"\[[a-zA-Z]{1,2}[0-9]{1,2}\|(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|[0-9]{4,}\]")
#  DEU|SEL|4sv
regexlist.append(r"(DEU|GBR|USA|FRA|CHN|KOR|MEX|NLD|EGY|PRT|CZE|SAU|NOR|MAR|AUT|TUR|ESP|POL|CAN|SVK|HUN|ZAF|BGR|HRV|TWN|NLD|ITA|THA|SWE|BRA|RUS|GRC|LBN)\|[a-z]{1,3}\|[a-z0-9]{3}")