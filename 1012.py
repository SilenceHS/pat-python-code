n=input()
sall=n.split()
a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
for i in range(1,len(sall)):
    all=int(sall[i])
    if all%5==0 and all%2==0:
        a1.append(all)
    if all%5==1:
        a2.append(all)
    if all%5==2:
        a3.append(all)
    if all%5==3:
        a4.append(all)
    if all%5==4:
        a5.append(all)
if len(a1)==0:
    A1='N'
else:
    A1=sum(a1)
if len(a2)==0:
    A2='N'
else:
    A2=0
    for i in range(len(a2)):
        A2+=a2[i]*(-1)**i
if len(a3)==0:
    A3='N'
else:
    A3=len(a3)
if len(a4)==0:
    A4='N'
else:
    A4=round(sum(a4)/len(a4),1)
if len(a5)==0:
    A5='N'
else: 
    A5=max(a5)
print(A1,A2,A3,A4,A5,sep=' ')
