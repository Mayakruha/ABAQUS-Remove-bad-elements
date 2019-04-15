#Comand line:
#      python CommmentElem.py <a file with a list of commented elements> <a file for changing>
import sys
import commands
#-----reading elements
fop=open(sys.argv[1])
ElemStr=[]
Elements=[]
line=fop.readline()
if "," in line:
	Sepr=","
else:
	Sepr=" "
ElemStr=ElemStr+line.split(Sepr)	
while True:
	line=fop.readline()
	ElemStr=ElemStr+line.split(Sepr)
	if not line:
		break
k=0
for i in ElemStr:
 	if (i!="") and (i!=" \n") and (i!="\r\n"):
		Elements.append(int(i))
 	 	k=k+1
print k, " elements must be commented"
fop.close()
#
#------writing comments
#
fop=open(sys.argv[2])
fw=open(sys.argv[2]+"~","w")
k=0
while True:
	line=fop.readline()
	if  len(line)>2:
		 if(line[0]=="*")and(line[1]!="*"):
		  	FlagElem=False
	if not line:
		break
	elif "**" in line:
		fw.write(line)
	elif  line.lower().startswith("*element") and not line.lower().startswith("*element output"):
        	FlagElem=True
		fw.write(line)
	elif FlagElem:
		ElemStr=line.split(",")
		ElNum=int(ElemStr[0])
		if ElNum in Elements:
			k=k+1
			fw.write("**"+line)
		else:
		 	fw.write(line)
	else:
		fw.write(line)	
fw.close()
fop.close()
print k, " elements have been commented"
commands.getoutput("rm "+sys.argv[2])
commands.getoutput("scp "+sys.argv[2]+"~ "+sys.argv[2])
commands.getoutput("rm "+sys.argv[2]+"~ ")
