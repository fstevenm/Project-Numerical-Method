an=2
bn=3
pn=(an+bn)/2
fan=(an**3)-25
fbn=(bn**3)-25
fpn=(pn**3)-25
print("solusi iterasi ke- 1 adalah",pn)
for i in range (2,1000):
    fpn=(pn**3)-25
    if fpn<0:
        an=pn
        pn=(an+bn)/2
        print("solusi iterasi ke-",i,"adalah",pn)
        if abs(fpn)<10**-4:
            break
    else:
        bn=pn
        pn=(an+bn)/2
        print("solusi iterasi ke-",i,"adalah",pn)
        if abs(fpn)<10**-4:
            break
        

    
    

