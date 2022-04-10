from trapesium import trapesium

a=0
b=1
n=4
def f(x):
    f=x**2
    return f

eksak=1/3
hampiran=trapesium(a,b,f,n)

salah=abs((eksak-hampiran)/eksak)

#print(hampiran)
#print(salah)

print('n={:d},solusi={:.16f},salah_relatif={:g}'.format(n,hampiran,salah))