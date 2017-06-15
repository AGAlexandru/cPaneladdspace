#!/usr/bin/python
users=open('users.txt','w')
import commands
import re
home2 = 0
if "home2" in commands.getoutput("df -h"):
	home2 = 1
homesize = commands.getoutput("df -h| grep /home | awk {'print $5'}")
homesize = re.findall('(.*?)%', homesize)
homesize = homesize[0]
homesize = int(homesize)
if homesize >= 95:
	if home2 == 0:
		exit()
if home2 == 1:
	home2size = commands.getoutput("df -h| grep /home2 | awk {'print $5'}")
	home2size = re.findall('(.*?)%', home2size)
	home2size = home2size[0]
	home2size = int(home2size)
	if home2size >= 95:
		if homesize >= 95:
			exit()
		else:
			home2 = 0
ids = commands.getoutput("ls -lh /home | awk {'print $3'}")
ids = ids.split( )
for id in ids:
	if id != "root":
		acc = commands.getoutput("whmapi1 accountsummary user="+id)
		if "reason: OK" in acc:
			disklimit = re.findall('disklimit: (.*?)M', acc)
			disklimit = disklimit[0]
			disklimit = int(disklimit)
			diskused = re.findall('diskused: (.*?)M', acc)
			diskused = diskused[0]
			diskused = int(diskused)
			diskfree = disklimit - diskused
			newdisk = disklimit + 1000     
			newdisk = str(newdisk)1
			if diskfree <= 200:
				ndiskcommand = "whmapi1 editquota user=" + id + " quota=" + newdisk
				commands.getoutput(ndiskcommand)        
				users.write(id +" " + newdisk +"\n")
if home2 == 1:
	ids = commands.getoutput("ls -lh /home2 | awk {'print $3'}")
	ids = ids.split( )
	for id in ids:
			if id != "root":
					acc = commands.getoutput("whmapi1 accountsummary user="+id)
					if "reason: OK" in acc:
							disklimit = re.findall('disklimit: (.*?)M', acc)
							disklimit = disklimit[0]
							disklimit = int(disklimit)
							diskused = re.findall('diskused: (.*?)M', acc)
							diskused = diskused[0]
							diskused = int(diskused)
							diskfree = disklimit - diskused         
							newdisk = disklimit + 1000
							newdisk = str(newdisk)
							if diskfree <= 200:
									ndiskcommand = "whmapi1 editquota user=" + id + " quota=" + newdisk
									commands.getoutput(ndiskcommand)
									users.write(id + "\n")
#github.com/AGAlexandru/
