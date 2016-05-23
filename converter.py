import os,subprocess

path = "./championships"
pathxml = "./convertall"
dirs = os.listdir(path)
for file in dirs:
  # if os.path.isdir(file):
  	newfolder = pathxml+ "/" + file;
  	print("dossier : " + file)
  	if(file=="stats.sh"):
  		break
  	if not os.path.exists(newfolder):
  		os.mkdir(newfolder)

  	dirs2 = os.listdir(path + "/"+ file)
  	for json in dirs2:
  		pathjson = path + "/"+ file + "/" + json
  		finalpath = newfolder + "/" + json + ".xml"
  		print("\t"+pathjson)
  		subprocess.call(["python2.7", "json22xml.py", pathjson, finalpath])

print("conversion reussie enregiste dans " + pathxml)