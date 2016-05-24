from lxml import etree
import sys
from xml.dom import minidom

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

listarg = ["fly", "heading", "echo", "scan", "stop", "land", "move_to", "scout", "glimpse", "explore", "exploit", "transform"]

#listarg = ["fly", "heading", "echo", "scan", "stop", "land", "move_to", "scout", "glimpse", "explore", "exploit", "transform"]
newdoc = minidom.Document()

if len(sys.argv) <2:
	print("Use : python parserxml.py [fichier.xml] [week]")

filename = sys.argv[1]

tree = etree.parse(filename)
root = tree.getroot()
currentAction = -1
for data in root.findall("data"):
	action = data.find("data").find("action")
	cost = data.find("data").find("cost")
	if(action != None):
		i=0
		for arg in listarg:
			if action.text == arg:
				currentAction = i
				break
			i=i+1
		
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

#print("number of fly : %d" % len(fly))
#print("number of heading : %d" % len(heading))
#print("number of echo : %d" % len(echo))
#print("number of scan : %d" % len(scan))
#print("number of stop : %d" % len(stop))
#print("number of land : %d" % len(land))
#print("number of move_to : %d" % len(move_to))
#print("number of scout : %d" % len(scout))
#print("number of glimpse : %d" % len(glimpse))
#print("number of explore : %d" % len(explore))
#print("number of exploit : %d" % len(exploit))
#print("number of transform : %d" % len(transform))


def createnode(tag, value):
	newdoc = minidom.Document()
	nn = newdoc.createElement(tag)
	value =  newdoc.createTextNode(value)
	nn.appendChild(value)
	return nn

def mymean(mylist):
	summ = 0;
	if len(mylist)==0:
		return 0
	for value in mylist:
		summ = summ + int(value)
	return summ/len(mylist)

def createaction(action, moyenne, longeur):
	act = newdoc.createElement(action)
	moy = createnode('moyenne', moyenne)
	lon = createnode('longeur', longeur)
	act.appendChild(moy)
	act.appendChild(lon)
	return act



def makeallactions(*lists):
	act = newdoc.createElement("list")
	i=0
	for mylist in lists:
		action = createaction(listarg[i], str(mymean(mylist)),  str(len(mylist)))
		act.appendChild(action)
		i=i+1
	return act

def makealldata(week, team):	
	newroot = newdoc.createElement('data')

	newroot.appendChild(createnode('team', team))
	newroot.appendChild(createnode('week', week))

	allactions = makeallactions(fly, heading, echo, scan, stop, land, move_to, scout, glimpse, explore, exploit, transform)
	newroot.appendChild(allactions)
	newdoc.appendChild(newroot)
	return newdoc


def writedata(newdoc):
	ff = open("data.xml", "r").read()
	doc = ff.split("</alldata>")[0]

	file = open("data.xml", "w");
	file.write(doc)
	newdata = newdoc.toprettyxml().replace("<?xml version=\"1.0\" ?>", "")
	file.write(newdata)
	file.write("</alldata>")
	file.close()

week = sys.argv[2]

team = sys.argv[1]
team = team.split(".")[1].split("/")
team = team[len(team)-1]
#print team


alldata = makealldata(week, team)
writedata(alldata)

#newroot.appendChild(weekxml)

#newroot = newdoc.createElement('alldata')

#newdoc.appendChild(newroot)




#file.write(newdoc.toprettyxml())

 #newdoc = minidom.Document()
  #newroot = newdoc.createElement('root')
 # rootattr = newdoc.createAttribute('name')
 # rootattr.nodeValue = 'foo'
#  newdoc.appendChild(newroot)

