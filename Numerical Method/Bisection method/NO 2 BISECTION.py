#an=-2
#bn=1.5
#pn=(an+bn)/2
#fan=3*(an+1)*(an-0.5)*(an-1)
#fbn=3*(bn+1)*(bn-0.5)*(bn-1)
#fpn=3*(pn+1)*(pn-0.5)*(pn-1)
#print("solusi iterasi ke- 1 adalah", pn)
#for i in range (2,4):
#    fpn=3*(pn+1)*(pn-0.5)*(pn-1)
#    if fpn<0:
#        an=pn
#        pn=(an+bn)/2
#        print("solusi iterasi ke-",i,"adalah", pn)
#        i=i+1
#    else:
#        bn=pn
#        pn=(an+bn)/2
#        print("solusi iterasi ke-",i,"adalah", pn)
#        i=i+1


an=0
bn=1
pn=(an+bn)/2
f = lambda x: 4*(x)**3-42*(x)**2+120*(x)-70

for i in range (1,3):
    if i == 1:
        print("interval ke-1","[{0},{1}]".format(an,bn))
        print("solusi iterasi ke- 1 adalah", f(pn))
        
    if f(pn)<0:
        an=pn
        print("interval ke",i+1,"[{0},{1}]".format(an,bn))
        pn=(an+bn)/2
        print("solusi iterasi ke-",i+1,"adalah", pn)
        i=i+1

    elif f(pn)>=0:
        bn=pn
        print("interval ke",i+1,"[{0},{1}]".format(an,bn))
        pn=(an+bn)/2
        print("solusi iterasi ke-",i+1,"adalah", pn)
        i=i+1