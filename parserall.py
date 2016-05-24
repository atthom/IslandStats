# -*- coding: utf-8 -*-
import os,subprocess

pathxml = "./convertall"
dirs = os.listdir(pathxml)
for week in dirs:
  dirs2 = os.listdir(pathxml + "/"+ week)
  print("semaine " + week)
  for xml in dirs2:
    file = pathxml + "/"+ week + "/" + xml
    print("\t"+xml)
    subprocess.call(["python2.7", "parserxml.py", file, week])

print("Calcul sauvegardé dans data.xml")