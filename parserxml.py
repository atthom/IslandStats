from lxml import etree

fly = []
heading = []
echo = []
scan = []
stop = []
land = []
move_to = []
scout = []
glimpse = []
explore = []
exploit = []
transform = []

tree = etree.parse("qae.xml")
root = tree.getroot()
currentAction = -1
for data in root.findall("data"):
	action = data.find("data").find("action")
	cost = data.find("data").find("cost")
	if(action != None):
		if (action.text == "fly"):
			currentAction = 0
		if (action.text == "heading"):
			currentAction = 1
		if (action.text == "echo"):
			currentAction = 2
		if (action.text == "scan"):
			currentAction = 3
		if (action.text == "stop"):
			currentAction = 4
		if (action.text == "land"):
			currentAction = 5
		if (action.text == "move_to"):
			currentAction = 6
		if (action.text == "scout"):
			currentAction = 7
		if (action.text == "glimpse"):
			currentAction = 8
		if (action.text == "explore"):
			currentAction = 9
		if (action.text == "exploit"):
			currentAction = 10
		if (action.text == "transform"):
			currentAction = 11

	if(cost!=None):
		if(currentAction == 0):
			fly.append(cost.text)
		if(currentAction == 1):
			heading.append(cost.text)
		if(currentAction == 2):
			echo.append(cost.text)
		if(currentAction == 3):
			scan.append(cost.text)
		if(currentAction == 4):
			stop.append(cost.text)
		if(currentAction == 5):
			land.append(cost.text)
		if(currentAction == 0):
			move_to.append(cost.text)
		if(currentAction == 7):
			scout.append(cost.text)
		if(currentAction == 8):
			glimpse.append(cost.text)
		if(currentAction == 9):
			explore.append(cost.text)
		if(currentAction == 10):
			exploit.append(cost.text)
		if(currentAction == 11):
			transform.append(cost.text)





print("number of fly : %d" % len(fly))
print("number of heading : %d" % len(heading))
print("number of echo : %d" % len(echo))
print("number of scan : %d" % len(scan))
print("number of stop : %d" % len(stop))
print("number of land : %d" % len(land))
print("number of move_to : %d" % len(move_to))
print("number of scout : %d" % len(scout))
print("number of glimpse : %d" % len(glimpse))
print("number of explore : %d" % len(explore))
print("number of exploit : %d" % len(exploit))
print("number of transform : %d" % len(transform))

