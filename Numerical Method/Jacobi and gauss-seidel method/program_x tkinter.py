import tkinter
import numpy as np


def getView():
    global koef_x11,koef_x12,koef_x13,koef_x14,koef_x21,koef_x22,koef_x23,koef_x24,koef_x31,koef_x32,koef_x33,koef_x34,koef_x41,koef_x42,koef_x43,koef_x44
    global koef_b1,koef_b2,koef_b3,koef_b4
    
    pilih=tkinter.Label(jendela_isi,font=("Arial 10 bold"),text="Masukkan nilai-nilai koefisien nya",
                                        bg='grey',fg='white',bd=5,
                                        width=30,justify=tkinter.CENTER)
    pilih.grid(row=0,column=0,columnspan=10)

    '''----------------Persamaan 2 ----------------'''
    '''----------------Persamaan 2 ----------------'''
    '''----------------Persamaan 2 ----------------'''
    
    koef_x11=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x11.grid(row=1,column=0,pady=4)
    
    koef_x12=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x12.grid(row=1,column=2)


    koef_x13=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x13.grid(row=1,column=4)
        
    koef_x14=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x14.grid(row=1,column=6)

    
    koef_b1=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_b1.grid(row=1,column=8)
    
    
    x11=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X1 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x11.grid(row=1,column=1)


    x12=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X2 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x12.grid(row=1,column=3)
    
    x13=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X3 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x13.grid(row=1,column=5)
    
    x14=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X4 =",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x14.grid(row=1,column=7)
    
    '''----------------Persamaan 2 ----------------'''
    '''----------------Persamaan 2 ----------------'''
    '''----------------Persamaan 2 ----------------'''
    
    koef_x21=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x21.grid(row=2,column=0,pady=4)
    
    koef_x22=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x22.grid(row=2,column=2)


    koef_x23=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x23.grid(row=2,column=4)
        
    koef_x24=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x24.grid(row=2,column=6)

    
    koef_b2=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_b2.grid(row=2,column=8)
    
    
    x21=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X1 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x21.grid(row=2,column=1)


    x22=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X2 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x22.grid(row=2,column=3)
    
    x23=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X3 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x23.grid(row=2,column=5)
    
    x24=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X4 =",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x24.grid(row=2,column=7)
    
    '''----------------Persamaan 3 ----------------'''
    '''----------------Persamaan 3 ----------------'''
    '''----------------Persamaan 3 ----------------'''
    
    koef_x31=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x31.grid(row=3,column=0,pady=4)
    
    koef_x32=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x32.grid(row=3,column=2)


    koef_x33=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x33.grid(row=3,column=4)
        
    koef_x34=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x34.grid(row=3,column=6)

    
    koef_b3=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_b3.grid(row=3,column=8)
    
    
    x31=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X1 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x31.grid(row=3,column=1)


    x32=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X2 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x32.grid(row=3,column=3)
    
    x33=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X3 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x33.grid(row=3,column=5)
    
    x34=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X4 =",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x34.grid(row=3,column=7)
    
    '''----------------Persamaan 4 ----------------'''
    '''----------------Persamaan 4 ----------------'''
    '''----------------Persamaan 4 ----------------'''
    
    koef_x41=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x41.grid(row=4,column=0,pady=4)
    
    koef_x42=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x42.grid(row=4,column=2)


    koef_x43=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x43.grid(row=4,column=4)
        
    koef_x44=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_x44.grid(row=4,column=6)

    
    koef_b4=tkinter.Entry(jendela_isi,font=("Arial 14 bold"),
                               bg='grey',fg='white',width=5,bd=2,
                                justify=tkinter.CENTER)
    koef_b4.grid(row=4,column=8)
    
    
    x41=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X1 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x41.grid(row=4,column=1)


    x42=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X2 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x42.grid(row=4,column=3)
    
    x43=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X3 +",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x43.grid(row=4,column=5)
    
    x44=tkinter.Label(jendela_isi,font=("Arial 14 bold"),text="X4 =",
                                bg='grey',fg='white',
                                width=5,justify=tkinter.CENTER)
    x44.grid(row=4,column=7)
    
    mulaigauss=tkinter.Button(jendela_isi,font=("Arial 10 bold"),text="Metode Gauss-Seidel",
                                        bg='grey',fg='white',bd=5,
                                        width=18,justify=tkinter.CENTER,command=ganti_2)
    mulaigauss.grid(row=5,column=7,columnspan=2)
    
    mulaijacobi=tkinter.Button(jendela_isi,font=("Arial 10 bold"),text="Metode Jacobi",
                                        bg='grey',fg='white',bd=5,
                                        width=18,justify=tkinter.CENTER,command=ganti_3)
    mulaijacobi.grid(row=5,column=0,columnspan=2)
    mulaijacobi['state']='disabled'
    
    space=tkinter.Label(jendela_isi,font=("Arial 10 bold"),
                                        bg='white',fg='white',
                                        width=18)
    space.grid(row=5,column=2,columnspan=2)
    space2=tkinter.Label(jendela_isi,font=("Arial 10 bold"),
                                        bg='white',fg='white',
                                        width=18)
    space2.grid(row=5,column=4,columnspan=2)

    return jendela_isi

def ganti_1():
    welcome.grid_forget()
    getView()
    

def ganti_2():
    global koef_x11,koef_x12,koef_x13,koef_x14,koef_x21,koef_x22,koef_x23,koef_x24,koef_x31,koef_x32,koef_x33,koef_x34,koef_x41,koef_x42,koef_x43,koef_x44
    global koef_b1,koef_b2,koef_b3,koef_b4
    global A,b,x
   
    jendela_isi.grid_forget()
    view.grid(row=1,column=0)
    text1=tkinter.Label(view,text="Thank you - St",bg="white")
    text1.grid()
    
    b11=int(koef_b1.get())
    
    A=np.array([[int(koef_x11.get()),int(koef_x12.get()),int(koef_x13.get()),int(koef_x14.get())]\
               ,[int(koef_x21.get()),int(koef_x22.get()),int(koef_x23.get()),int(koef_x24.get())]\
               ,[int(koef_x31.get()),int(koef_x32.get()),int(koef_x33.get()),int(koef_x34.get())]\
               ,[int(koef_x41.get()),int(koef_x42.get()),int(koef_x43.get()),int(koef_x44.get())]])
    b=np.array([b11,int(koef_b2.get()),int(koef_b3.get()),int(koef_b4.get())])
    x = np.array([0,0,0,0])

    seidel(A,x,b)
    
    
def ganti_3():
    global koef_x11,koef_x12,koef_x13,koef_x14,koef_x21,koef_x22,koef_x23,koef_x24,koef_x31,koef_x32,koef_x33,koef_x34,koef_x41,koef_x42,koef_x43,koef_x44
    global koef_b1,koef_b2,koef_b3,koef_b4
    global A,b,x
   
    jendela_isi.grid_forget()
    view.grid(row=1,column=0)
    text1=tkinter.Label(view,text="Thank you - St",bg="white")
    text1.grid()
    
    b11=int(koef_b1.get())
    
    A=np.array([[int(koef_x11.get()),int(koef_x12.get()),int(koef_x13.get()),int(koef_x14.get())]\
               ,[int(koef_x21.get()),int(koef_x22.get()),int(koef_x23.get()),int(koef_x24.get())]\
               ,[int(koef_x31.get()),int(koef_x32.get()),int(koef_x33.get()),int(koef_x34.get())]\
               ,[int(koef_x41.get()),int(koef_x42.get()),int(koef_x43.get()),int(koef_x44.get())]])
    b=np.array([b11,int(koef_b2.get()),int(koef_b3.get()),int(koef_b4.get())])
    x = np.zeros(4)

    jacobi(A,x,b)


def jacobi(A, b, x_awal, toleransi=10**-3):
    global koef_x11,koef_x12,koef_x13,koef_x14,koef_x21,koef_x22,koef_x23,koef_x24,koef_x31,koef_x32,koef_x33,koef_x34,koef_x41,koef_x42,koef_x43,koef_x44
    global koef_b1,koef_b2,koef_b3,koef_b4
    global x_iterasi
#    x=np.array([0,0,0,0])
    x_iterasi=[x]
    
    while len(x_iterasi)<2 or panjang_vektor(x_iterasi[-1]-x_iterasi[-2])/panjang_vektor(x_iterasi[-1])>=toleransi:
        x_baru=np.zeros(len(b))
        for i in range(len(b)):
            jumlah=0
            for j in range(len(b)):
                if i!=j:
                    jumlah-=A[i][j]*x_iterasi[-1][j]
            x_baru[i]=1/A[i][i]*(jumlah+b[i])
        x_iterasi.append(x_baru)
        
    for it in range(len(x_iterasi)): #menampilkan iterasi
        print('Iterasi ke-'+str(it)+':',x_iterasi[it])
    return x_iterasi[-1]


def seidel(a, x ,b, toleransi=10**(-3)):
    global koef_x11,koef_x12,koef_x13,koef_x14,koef_x21,koef_x22,koef_x23,koef_x24,koef_x31,koef_x32,koef_x33,koef_x34,koef_x41,koef_x42,koef_x43,koef_x44
    global koef_b1,koef_b2,koef_b3,koef_b4
    global x_iterasi
    hasil.grid(row=0,column=0)
    
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
        
    iterasi=tkinter.Label(hasil,text="iterasi")
    iterasi.grid(row=0,column=0)
    x1=tkinter.Label(hasil,text="x1")
    x1.grid(row=0,column=1)
    x2=tkinter.Label(hasil,text="x2")
    x2.grid(row=0,column=2)
    x3=tkinter.Label(hasil,text="x3")
    x3.grid(row=0,column=3)
    x4=tkinter.Label(hasil,text="x4")
    x4.grid(row=0,column=4)
    
    
    for ite in range (len(x_iterasi)):
        if ite>=11:
            literasi=tkinter.Label(hasil,text=(len(x_iterasi)+1))
            literasi.grid(row=ite+1,column=0)
            matriks_n0=tkinter.Label(hasil,text=(x_iterasi[-1][0]))
            matriks_n1=tkinter.Label(hasil,text=(x_iterasi[-1][1]))
            matriks_n2=tkinter.Label(hasil,text=(x_iterasi[-1][2]))
            matriks_n3=tkinter.Label(hasil,text=(x_iterasi[-1][3]))
            matriks_n0.grid(row=ite+2,column=1)
            matriks_n1.grid(row=ite+2,column=2)
            matriks_n2.grid(row=ite+2,column=3)
            matriks_n3.grid(row=ite+2,column=4)
            break
#        print("{:11d} {:20f} {:20f} {:20f} {:20f}".format(ite,x_iterasi[ite][0],x_iterasi[ite][1],x_iterasi[ite][2],x_iterasi[ite][3]))
        literasi=tkinter.Label(hasil,text=ite)
        matriks_0=tkinter.Label(hasil,text=(x_iterasi[ite][0]))
        matriks_1=tkinter.Label(hasil,text=(x_iterasi[ite][1]))
        matriks_2=tkinter.Label(hasil,text=(x_iterasi[ite][2]))
        matriks_3=tkinter.Label(hasil,text=(x_iterasi[ite][3]))
        literasi.grid(row=ite+1,column=0)
        matriks_0.grid(row=ite+1,column=1)
        matriks_1.grid(row=ite+1,column=2)
        matriks_2.grid(row=ite+1,column=3)
        matriks_3.grid(row=ite+1,column=4)
        
    return x_iterasi[-1]

def panjang_vektor(x): #panjang vektor
    nilai=0
    for i in x:
        nilai+=i**2
    return nilai**(1/2)


def bg():
    canvas = tkinter.Canvas(jendela1,bg='black',
                            width=800,height=280)
    canvas.grid(row=0,column=0)
    gambarbaru = tkinter.PhotoImage(file='download.png')
    canvas.create_image(400,60, image=gambarbaru)
    canvas.image=gambarbaru


window=tkinter.Tk()

window.geometry("843x350")
window.title("mencari nilai x")
window.configure(bg='black')
gambar_jendela=tkinter.PhotoImage(file='download.png')

jendela1 = tkinter.Frame(window,bd=20)
jendela1.grid()
bg()
view=tkinter.Frame(window)
hasil=tkinter.Frame(jendela1)

jendela_isi = tkinter.Frame(jendela1,bg='white',bd=20,width=900,height=200)
jendela_isi.grid(row=0,column=0)

welcome=tkinter.Button(jendela_isi,text="SELAMAT DATANG",width=50,command=ganti_1)
welcome.grid(row=0,column=0)


window.mainloop()
