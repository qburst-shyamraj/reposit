import math
x1=967
y1=967
x2=257
y2=724
m=int((y1-y2)/(x1-x2))
xin=153
for yin in range(193,806,1):
	if (y2-yin)/(x2-xin)==m:
		break
print(xin,yin)
vax=xin-x2
vay=yin-y2
ang=abs(math.atan2(vay,vax))
ang*=180/3.14
print(int(ang))
dist1=math.sqrt((x2-xin)**2+(y2-yin)**2)
dist2=math.sqrt((x1-x2)**2+(y1-y2)**2)
force1=2*dist1*1+300
force2=2*dist2*2+600
force=force1+force2
print (force)

