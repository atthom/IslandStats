# -*- coding: utf-8 -*-
import sys
from xml.dom import minidom

doc = minidom.parse("data.xml")

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

listaction = ["fly", "heading", "echo", "scan", "stop", "land", "move_to", "scout", "glimpse", "explore", "exploit", "transform"]
listweek = ["week01", "week02", "week04", "week05", "week06", "week07", "week10", "week11", "week12", "week46", "week47", "week48",  "week49", "week50", "week5",  "wee52",  "week53"]
listteam = ["qaa",  "qac",  "qae",  "qba",  "qbc",  "qbf",  "qcb",  "qce",  "qdb",  "qdd", "qab",  "qad",  "qaf",  "qbb",  "qbe",  "qca",  "qcc",  "qda",  "qdc",  "qde", "qdf"]

alldata = doc.getElementsByTagName("data")

def getelement(data, key):
	return data.getElementsByTagName(key)[0].firstChild.data
def dataaction(action):
	allaction = doc.getElementsByTagName(action)
	sum_mean= 0.0
	sum_long= 0.0
	for act in allaction:
		current_long = int(getelement(act,"longeur"))
		current_moy = float(getelement(act,"moyenne"))
		if current_long!=0:
			sum_mean = float(sum_mean*float(sum_long) + current_moy*float(current_long))/float(sum_long  + current_long)
			sum_long= sum_long + current_long

	if sum_long==0:
		print "L'action %s n'a pas été utilisé" % (action)
	else:
		print "il y a eu %d %s, de coup moyen %f et de coup total %f" % (sum_long, action, sum_mean, sum_mean*sum_long)
	nbaction =0;

for act in listaction:
	dataaction(act)
#for action in listaction:
#	alldataforaction = doc.getElementsByTagName(action)


def tauxdereussiteglobal():
	nbrun = len(alldata)
	nbstop = 0
	for stp in doc.getElementsByTagName("stop"):
		nbstop = nbstop + int(getelement(stp, "longeur"))

	taux = float(nbstop) / float(nbrun)
	
	print "Il y a eu %d explorations avec %d réussie, donc un taux de réussite de %f " % (nbrun, nbstop, taux)

tauxdereussiteglobal()

def goodteamgoodweek(datateam, dataweek, team="", week=""):
	if team!="" and datateam!=team:
		return False
	if week!="" and dataweek!=week:
		return False
	return True


def tauxdereussite(team="", week=""):
	nbstop = 0
	nbrun = 0
	for data in alldata:
		datateam = data.getElementsByTagName("team")
		dataweek = data.getElementsByTagName("week")
		print dataweek
		if goodteamgoodweek(datateam, dataweek, team, week) is True:
			stp = data.getElementsByTagName("stop")
			nbstop = nbstop + int(getelement(stp, "longeur"))
			nbrun = nbrun +1
	taux = float(nbstop) / float(nbrun)
	print "Il y a eu %d explorations avec %d réussie, donc un taux de réussite de %f " % (nbrun, nbstop, taux)


def tauxdereussitebyteam(team):
	nbstop = 0
	nbrun = 0
	for data in alldata:
		for wee in data.getElementsByTagName("week"):
				for teamdata in data.getElementsByTagName("team"):
					if teamdata.firstChild.data==team:						
						stp = data.getElementsByTagName("stop")[0]
						nbstop = nbstop + int(getelement(stp, "longeur"))
						nbrun = nbrun +1
	if nbrun!=0:
		taux = float(nbstop) / float(nbrun)
		print "Il y a eu %d explorations pour l'équipe %s avec %d réussie, donc un taux de réussite de %f " % (nbrun, team, nbstop, taux)

def tauxdereussitebyweek(week):
	nbstop = 0
	nbrun = 0
	for data in alldata:
		for teamdata in data.getElementsByTagName("team"):
				for wee in data.getElementsByTagName("week"):
					if wee.firstChild.data==week:						
						stp = data.getElementsByTagName("stop")[0]
						nbstop = nbstop + int(getelement(stp, "longeur"))
						nbrun = nbrun +1
	if nbrun!=0:
		taux = float(nbstop) / float(nbrun)
		print "Au cours de la semaine %s, Il y a eu %d explorations avec %d réussie, donc un taux de réussite de %f " % (week, nbrun, nbstop, taux)

def dataaction(week):
	alldata = doc.getElementsByTagName("data")
	sum_mean= 0.0
	sum_long= 0.0
	for data in alldata:
		current_long = int(getelement(act,"longeur"))
		current_moy = float(getelement(act,"moyenne"))
		if current_long!=0:
			sum_mean = float(sum_mean*float(sum_long) + current_moy*float(current_long))/float(sum_long  + current_long)
			sum_long= sum_long + current_long

	if sum_long==0:
		print "L'action %s n'a pas été utilisé" % (action)
	else:
		print "il y a eu %d %s, de coup moyen %f et de coup total %f" % (sum_long, action, sum_mean, sum_mean*sum_long)
	nbaction =0;

def tauxdereussitedetail():
	print "\n****************\n"
	for team in listteam:
		tauxdereussitebyteam(team)
	print "\n****************\n"
	for week in listweek:
		tauxdereussitebyweek(week)


tauxdereussitedetail()