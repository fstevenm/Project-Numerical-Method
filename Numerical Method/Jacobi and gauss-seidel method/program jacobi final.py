import numpy as np

def jacobi(A, b, x_awal, toleransi=10**-3):
    global n
    diagonal = np.diag(np.diag(A))
    nilai_koef = A - diagonal
    
    x = x_awal
    x_baru=np.ones(len(b))
    a=x_baru - x
    
    while  np.linalg.norm(a, np.inf)/np.linalg.norm(x_baru, np.inf)> toleransi:
        koef_d = np.diag(1 / np.diag(diagonal))
        x_baru = np.dot(koef_d, b - np.dot(nilai_koef, x))
        a = x_baru - x
        x = x_baru
        n+=1
        print("{:11d} {:20f} {:20f} {:20f} {:20f}".format(n,x[0],x[1],x[2],x[3]))
        
    if np.linalg.norm(a, np.inf)/np.linalg.norm(x_baru, np.inf) < toleransi:
        koef_d = np.diag(1 / np.diag(diagonal))
        x_baru = np.dot(koef_d, b - np.dot(nilai_koef, x))
        a = x_baru - x
        x = x_baru
        n+=1
        print("{:11d} {:20f} {:20f} {:20f} {:20f}".format(n,x[0],x[1],x[2],x[3]))
        
    return x

#data soal
A = np.array([[10, -1, 2, 0]\
              ,[-1, 11, -1, 3]\
              ,[2, -1, 10, -1]\
              ,[0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])

#print persamaan
#print("SPL nya :")
#e1="10x1 -   x2 +  2x3       =  6"
#e2="-1x1 + 11x2 -   x3 + 3x4 =  25"
#e3=" 2x1 -   x2 + 10x3 -  x4 = -11"
#e4="        3x2 -   x3 + 8x4 =  15"
#print(e1,"\n",e2,"\n",e3,"\n",e4,"\n")

#vektor awal
x_awal = np.zeros(len(b))

n=0

print("\titerasi \t\t  x1 \t\t     x2 \t\t        x3 \t\t          x4 ")
print("{:11d} {:20f} {:20f} {:20f} {:20f}".format(n,x_awal[0],x_awal[1],x_awal[2],x_awal[3]))
x = jacobi(A, b, x_awal)

print("\nx : ("+str(x[0])+" ,",x[1],",",x[2],", "+str(x[3])+")")
print('\nnilai b dengan x di atas:', np.dot(A, x))
print('nilai asli b:', b)

