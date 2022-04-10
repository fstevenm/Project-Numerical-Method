
import numpy as np

def seidel(a,b,x0,E): #a matriks, b list, x0 list
    global x_iterasi
    x_iterasi=[x0]
    while len(x_iterasi)<2 or np.linalg.norm(x_iterasi[-1]-x_iterasi[-2])/np.linalg.norm(x_iterasi[-1])>=E:
        x_baru=np.zeros(len(x0))
        for i in range(len(x0)):
            sigma1=0
            sigma2=0
            for j in range(i):
                sigma1-=a[i][j]*x_baru[j]
            for j in range(i+1,len(x0)):
                sigma2-=a[i][j]*x_iterasi[-1][j]
            x_baru[i]=1/a[i][i]*(sigma1+sigma2+b[i])
        x_iterasi.append(x_baru)
#    for it in range(len(x_iterasi)): #menampilkan iterasi
#        print('Iterasi ke-'+str(it)+':',x_iterasi[it])
    return x_baru

