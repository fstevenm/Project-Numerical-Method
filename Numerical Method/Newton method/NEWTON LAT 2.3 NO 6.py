print("**********************************************")
print("\t \t NO 6a")
print("**********************************************")
from numpy import e,log,cos,sin
p0=1
for i in range(1,1000):
    a=(e**p0)+(2**-p0)+(2*cos(p0))-6
    b=(e**p0)-(log(2)/2**p0)-(2*sin(p0))
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1    
print()
print()

print("**********************************************")
print("\t \t NO 6b")
print("**********************************************")
from numpy import log,cos,sin
p0=1.3
for i in range(1,1000):
    a=(log(p0-1))+(cos(p0-1))
    b=(1/(p0-1))-(sin(p0-1))
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1
print()
print()

print("**********************************************")
print("\t \t NO 6c")
print("**********************************************")
from numpy import cos,sin
p0=2
for i in range(1,1000):
    a=(2*p0*cos(2*p0))-(p0-2)**2
    b=(2*cos(2*p0))-(4*p0)*sin(2*p0)-2*p0+4
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1
print()
print()
print("**********************************************")
from numpy import cos,sin
p0=4
for i in range(1,1000):
    a=(2*p0*cos(2*p0))-(p0-2)**2
    b=(2*cos(2*p0))-(4*p0)*sin(2*p0)-2*p0+4
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1
print()
print()

print("**********************************************")
print("\t \t NO 6d")
print("**********************************************")
from numpy import log
p0=2
for i in range(1,1000):
    a=(p0-2)**2-(log(p0))
    b=(2*p0-4)-(1/p0)
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1
print()
print()
print("**********************************************")
from numpy import log
p0=4
for i in range(1,1000):
    a=(p0-2)**2-(log(p0))
    b=(2*p0-4)-(1/p0)
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1
print()
print()

print("**********************************************")
print("\t \t NO 6e")
print("**********************************************")
from numpy import e
p0=1
for i in range(1,1000):
    a=(e**p0)-3*(p0**2)
    b=(e**p0)-6*p0
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1
    
print()
print()
print("**********************************************")
from numpy import e
p0=3
for i in range(1,1000):
    a=(e**p0)-3*(p0**2)
    b=(e**p0)-6*p0
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1
print()
print()

print("**********************************************")
print("\t \t NO 6f")
print("**********************************************")
from numpy import sin,e
p0=1
for i in range(1,1000):
    a=sin(p0)-(e**-p0)
    b=cos(p0)+(e**-p0)
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1
print()
print()
print("**********************************************")
from numpy import sin,e
p0=3
for i in range(1,1000):
    a=sin(p0)-(e**-p0)
    b=cos(p0)+(e**-p0)
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1
print()
print()

print("**********************************************")
from numpy import sin,e
p0=6
for i in range(1,1000):
    a=sin(p0)-(e**-p0)
    b=cos(p0)+(e**-p0)
    p1=p0-(a/b)
    print("solusi iterasi ke-",i,"adalah",p1)
    if abs(p1-p0)<10**-5:
        break
    p0=p1



    
