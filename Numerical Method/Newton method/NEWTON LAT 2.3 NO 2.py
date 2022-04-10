from math import sin,cos
p0=-1
for i in range(1,3):
    a=-(p0**3)-cos(p0)
    b=-(3*(p0**2))+sin(p0)
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    p0=p1
    
    
