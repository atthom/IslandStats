# -*- coding: utf-8 -*-
import os,subprocess

pathxml = "./convertall"
os.remove("data.xml")

data = open("data.xml", "w")
data.write("<?xml version=\"1.0\" ?>\n<alldata></alldata>")
data.close()

dirs = os.listdir(pathxml)
for week in dirs:
  dirs2 = os.listdir(pathxml + "/"+ week)
  print("semaine " + week)
  for xml in dirs2:
    file = pathxml + "/"+ week + "/" + xml
    print("\t"+xml)
    subprocess.call(["python2.7", "parserxml.py", file, week])

print("Calcul sauvegardé dans data.xml")