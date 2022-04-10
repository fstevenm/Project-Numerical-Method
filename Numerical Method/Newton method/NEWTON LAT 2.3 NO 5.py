"""no 5a"""
p0=1
for i in range(1,1000):
    a=(p0**3)-(2*(p0**2))-5
    b=(3*(p0**2))-(4*p0)
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-4:
        break
    p0=p1 
print() 
    
"""no 5b"""
p0=-3
for i in range(1,1000):
    a=(p0**3)+(3*(p0**2))-1
    b=(3*(p0**2))+(6*p0)
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-4:
        break
    p0=p1
print()


"""no 5c"""
from math import sin,cos
p0=0
for i in range(1,1000):
    a=p0-cos(p0)
    b=1+sin(p0)
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-4:
        break
    p0=p1
print()


"""no 5d"""
p0=0
for i in range(1,1000):
    a=p0-0.8-(0.2*sin(p0))
    b=1-(0.2*cos(p0))
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-4:
        break
    p0=p1
        
    
