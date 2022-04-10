# Defining our function as seidel which takes 3 arguments 
# as A matrix, Solution and B matrix 

import numpy as np

def panjang_vektor(x): #panjang vektor
    nilai=0
    for i in x:
        nilai+=i**2
    return nilai**(1/2)

def seidel(a, x ,b, toleransi=10**(-3)):
    n = len(a)
    x_iterasi=[x]
    x_baru=np.zeros(len(b))
    while len(x_iterasi)<2 or panjang_vektor(x_iterasi[-1]-x_iterasi[-2])/panjang_vektor(x_iterasi[-1])>= toleransi:
        for j in range(0, n):        
            d = b[j]                 
            for i in range(0, n):    
                if(j != i): 
                    d-=a[j][i] * x_baru[i]
            x_baru[j] = d / a[j][j]
        x_iterasi.append(np.array(x_baru))
    for ite in range (len(x_iterasi)):
        print("{:11d} {:20f} {:20f} {:20f} {:20f}".format(ite,x_iterasi[ite][0],x_iterasi[ite][1],x_iterasi[ite][2],x_iterasi[ite][3]))

    return x_iterasi[-1]     

# data                      
a = np.array([[10, -1, 2, 0]\
              ,[-1, 11, -1, 3]\
              ,[2, -1, 10, -1]\
              ,[0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])
     
x = np.array([0,0,0,0])

print("\titerasi \t\t  x1 \t\t     x2 \t\t        x3 \t\t          x4 ")

z=seidel(a,x,b)
print("\nJadi nilai x nya adalah ("+str(z[0])+" ,",z[1],",",z[2],", "+str(z[3])+")")
print('Nilai b dengan x di atas: (',np.dot(a, z)[0],np.dot(a, z)[1],np.dot(a, z)[2],np.dot(a, z)[3],")")

#for i in range(0, 5):           
#    x = seidel(a, x, b) 
#    #print each time the updated solution 
#    print(x)                     
