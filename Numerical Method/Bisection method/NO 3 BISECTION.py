an=-1.25
bn=2.5
pn=(an+bn)/2
fan=3*(an+1)*(an-0.5)*(an-1)
fbn=3*(bn+1)*(bn-0.5)*(bn-1)
fpn=3*(pn+1)*(pn-0.5)*(pn-1)
print("solusi iterasi ke- 1 adalah", pn)
for i in range (2,4):
    fpn=3*(pn+1)*(pn-0.5)*(pn-1)
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
    
        