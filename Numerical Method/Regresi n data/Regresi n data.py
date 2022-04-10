import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from gausseidel import seidel


# data asli
n=int(input("Berapa jumlah data yang diketahui :"))
xp1=[]
yp1=[]
for i in range (n):
    xi=float(input("Masukkan nilai x"+str(i+1)+" : "))
    yi=float(input("Masukkan nilai y"+str(i+1)+" : "))
    print("")
    xp1.append(xi)
    yp1.append(yi)
xp=np.array(xp1)
yp=np.array(yp1)
m=len(xp)


# menghitung konstanta-konstanta
derajat=int(input("Derajat berapa :"))


#PERSAMAANNYA
epers=[]
a=0
for c in range (derajat*2+1):
    jumlah=0
    while a==c:
        for i in range (n):
            ei=xp[i]**a
            jumlah+=ei
        epers.append(jumlah)
        break
    a+=1
#print(epers)
    
    
#MATRIKSNYA
A=[]
banyak=int(derajat)+1
for koe in range (derajat+1):
    akoe=np.array(epers[koe:koe+banyak])
    A.append(akoe)
#print(np.array(A))


#NILAI PERS NYA
b=[]
konstanta=0
for nilai in range (derajat+1):
    jumlah=0
    while konstanta==nilai:
        for i in range (n):
            bi=yp[i]*xp[i]**konstanta
            jumlah+=bi
        b.append(jumlah)
        konstanta+=1
#print(np.array(b))
  

#APROKSIMASI NILAI a
x=np.zeros(derajat+1)
#for nilai in range (derajat+1):
#    x.append(0)
#print(x)

polinomial=0
simbol_x=sym.symbols('x')
c=0
#print(seidel(A, b, x, 10**-5))
for angka in range (derajat+1):
    polinomial+=seidel(A, b, x, 10**-5)[angka]*simbol_x**c
    print("Koefisien a"+str(angka)+" =",seidel(A, b, x, 10**-5)[angka])
    c+=1
    
print("\nKita peroleh persamaannya yaitu :",polinomial)

fungsi_lambdify=sym.lambdify([simbol_x],polinomial)
Y=[]
for ulang in range(len(xp)):
    Y.append(fungsi_lambdify(xp[ulang]))

# menghitung error/kesalahan
print("")
simpangan=yp-Y
for i in range (len(simpangan)):
    print("besar simpangan data asli y"+str(i+1)+" dan hampirannya :",simpangan[i])
    
salah=sum(abs(yp-Y)**2) #menghitung total kesalahan
print("\ntotal errornya: ",salah)


# menggambar grafik
x_n=np.arange(min(xp),max(xp),0.001)
y=[]

for z in x_n:
    y.append(fungsi_lambdify(z))

plt.plot(xp,yp,'ro',x_n,y,'b')
plt.legend(['data asli','polinomial kuadrat terkecil linier'],loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([min(xp)-0.1,max(xp)+0.1,(min(Y) or min(yp))-1,(max(Y) or max(yp))+1])
plt.grid()
plt.title('Polinomial kuadrat terkecil linier')
plt.show()






