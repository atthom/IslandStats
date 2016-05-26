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
listweek = ["week46", "week47", "week48",  "week49", "week50", "week51",  "wee52",  "week53", "week01", "week02", "week04", "week05", "week06", "week07","week08" "week09", "week10", "week11", "week12"]
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
		print "il y a eu %d %s, de coup moyen %f et de coup total %f" % (sum_long, action, sum_mean, float(sum_mean)*float(sum_long))
	nbaction =0;

def tauxdereussiteglobal():
	nbrun = len(alldata)
	nbstop = 0
	for stp in doc.getElementsByTagName("stop"):
		nbstop = nbstop + int(getelement(stp, "longeur"))

	taux = float(nbstop) / float(nbrun)
	
	print "Il y a eu %d explorations avec %d réussie, donc un taux de réussite de %f%% " % (nbrun, nbstop, taux*100)



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
	print "Il y a eu %d explorations avec %d réussie, donc un taux de réussite de %f%% " % (nbrun, nbstop, taux*100)


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
		print "Il y a eu %d explorations pour l'équipe %s avec %d réussie, donc un taux de réussite de %f%% " % (nbrun, team, nbstop, taux*100)

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
		print "Au cours de la semaine %s, Il y a eu %d explorations avec %d réussie, donc un taux de réussite de %f%% " % (week, nbrun, nbstop, taux*100)

def dataweek(week):
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

def globalaction():
	sum_cost = 0.0
	sum_long = 0.0
	for action in listaction:
		allaction = doc.getElementsByTagName(action)
		for act in allaction:
			current_long = int(getelement(act,"longeur"))
			current_moy = float(getelement(act,"moyenne"))
			if current_long!=0:
				sum_cost = sum_cost + float(current_long)*current_moy
				sum_long = sum_long + current_long

	print "Il y a eu %d actions de coup total %f" % (sum_long, sum_cost)


def getnbactionandtotalcostbyaction(action):
	sum_cost = 0.0
	sum_long = 0
	allaction = doc.getElementsByTagName(action)
	for act in allaction:
		current_long = int(getelement(act,"longeur"))
		current_moy = float(getelement(act,"moyenne"))
		if current_long!=0:
			sum_cost = sum_cost + float(current_long)*current_moy
			sum_long = sum_long + current_long
	return [sum_cost, sum_long]

def globaltauxactions():
	sum_cost = 0.0
	sum_long = 0
	listall = []
	actionrate = []
	for action in listaction:
		listall.append(getnbactionandtotalcostbyaction(action))
	for oneact in listall:
		sum_cost = sum_cost + oneact[0]
		sum_long = sum_long + oneact[1]
	for action in listall:
		rate_cost = float(action[0]) / float(sum_cost)
		rate_long = float(action[1]) / float(sum_long)
		actionrate.append([rate_cost, rate_long])
	i =0
	for rate in actionrate:
		print "L'action %s a un taux d'utilisation de %f%%  et un taux de cout de %f%%" % (listaction[i], rate[1]*100, rate[0]*100)
		i = i+1
	print "\nIl y a eu au total %d actions pour un coup total de %d et un coup moyen de %f par actions" % (sum_long, sum_cost, float(sum_cost)/float(sum_long) )

def tauxdereussitedetail():
	for team in listteam:
		tauxdereussitebyteam(team)
	print "\n****************\n"
	for week in listweek:
		tauxdereussitebyweek(week)

for act in listaction:
	dataaction(act)

print "\n****************\n"

tauxdereussiteglobal()
print "\n****************\n"

tauxdereussitedetail()
print "\n****************\n"
globaltauxactions()