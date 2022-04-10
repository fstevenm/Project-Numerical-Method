def trapesium(a,b,f,n):
    h=(b-a)/n
    jumlah=0
    for i in range(1,n):
        x=a+i*h
        jumlah=jumlah+f(x)
    hasil=h/2*(f(a)+2*jumlah+f(b))
    return hasil

