from math import sqrt, cos
an=0
bn=1
pn=(an+bn)/2
fan=sqrt(an)-cos(an)
fbn=sqrt(bn)-cos(bn)
fpn=sqrt(pn)-cos(pn)
print("solusi iterasi ke- 1 adalah", pn)
for i in range (2,4):
    fpn=sqrt(pn)-cos(pn)
    if fpn<0:
        an=pn
        pn=(an+bn)/2
        print("solusi iterasi ke-",i,"adalah", pn)
        i=i+1
    else:
        bn=pn
        pn=(an+bn)/2
        print("solusi iterasi ke-",i,"adalah", pn)
        i=i+1
    
        