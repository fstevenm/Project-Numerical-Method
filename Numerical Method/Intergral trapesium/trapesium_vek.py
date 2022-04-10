from numpy import linspace

def trapesium_vek(a,b,f,n):
    h=(b-a)/n
    x=linspace(a,b,n+1)
    hasil=h/2*(2*sum(f(x))-f(a)-f(b))
    return hasil
               
    