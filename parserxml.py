from lxml import etree

stat_number_action = [0,0,0,0,0,0,0,0,0,0,0,0]
nb_action = 0;
tree = etree.parse("qae.xml")
for data in tree.xpath("/alldata/data/data/action"):
	nb_action+=1;
	if (data.text == "fly"):
		stat_number_action[0] = stat_number_action[0] + 1
	if (data.text == "heading"):
		stat_number_action[1] = stat_number_action[1] + 1
	if (data.text == "echo"):
		stat_number_action[2] = stat_number_action[2] + 1
	if (data.text == "scan"):
		stat_number_action[3] = stat_number_action[3] + 1
	if (data.text == "stop"):
		stat_number_action[4] = stat_number_action[4] + 1
	if (data.text == "land"):
		stat_number_action[5] = stat_number_action[5] + 1
	if (data.text == "move_to"):
		stat_number_action[6] = stat_number_action[6] + 1
	if (data.text == "scout"):
		stat_number_action[7] = stat_number_action[7] + 1
	if (data.text == "glimpse"):
		stat_number_action[8] = stat_number_action[8] + 1
	if (data.text == "explore"):
		stat_number_action[9] = stat_number_action[9] + 1
	if (data.text == "exploit"):
		stat_number_action[10] = stat_number_action[10] + 1
	if (data.text == "transform"):
		stat_number_action[11] = stat_number_action[11] + 1
print("number of fly : %d" % stat_number_action[0])
print("number of heading : %d" % stat_number_action[1])
print("number of echo : %d" % stat_number_action[2])
print("number of scan : %d" % stat_number_action[3])
print("number of stop : %d" % stat_number_action[4])
print("number of land : %d" % stat_number_action[5])
print("number of move_to : %d" % stat_number_action[6])
print("number of scout : %d" % stat_number_action[7])
print("number of glimpse : %d" % stat_number_action[8])
print("number of explore : %d" % stat_number_action[9])
print("number of exploit : %d" % stat_number_action[10])
print("number of transform : %d" % stat_number_action[11])
print("number of action : %d" % nb_action)
