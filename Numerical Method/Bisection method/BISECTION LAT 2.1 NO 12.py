""" mencari aproksimasi untuk √3 dengan relative error 10**-4"""
an=1
bn=2
pn=(an+bn)/2
fan=(an**2)-3
fbn=(bn**2)-3
fpn=(pn**2)-3
print("solusi iterasi ke- 1 adalah",pn)
for i in range (2,1000):
    fpn=(pn**2)-3
    if (fan*fbn)<0:
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
        

    
    

