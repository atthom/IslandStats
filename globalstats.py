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


def dataaction(action):
	allaction = doc.getElementsByTagName(action)
	sum_mean= 0.0
	sum_long= 0.0
	for act in allaction:
		current_long = int(act.getElementsByTagName("longeur")[0].firstChild.data)
		current_moy = float(act.getElementsByTagName("moyenne")[0].firstChild.data)
		if current_long!=0:
			sum_mean = float(sum_mean*float(sum_long) + current_moy*float(current_long))/float(sum_long  + current_long)
			sum_long= sum_long + current_long

	if sum_long==0:
		print "L'action %s n'a pas été utilisé" % (action)
	else:
		print "il y a eu %d %s, de coup moyen %f et de coup total %f" % (sum_long, action, sum_mean, sum_mean*sum_long)
	nbaction =0;


dataaction(listaction[0])
#for action in listaction:
#	alldataforaction = doc.getElementsByTagName(action)


