from trapesium_vek import trapesium_vek

a=0
b=1

def f(x):
    f=x**2
    return f

eksak=1/3
print('      n    hampiran        salah_rel')
for n in range(1,10):
    hampiran=trapesium_vek(a,b,f,n)
    salah=abs((eksak-hampiran)/eksak)
    print('{:7d} {:.16f} {:7.3f}'.format(n,hampiran,salah))

