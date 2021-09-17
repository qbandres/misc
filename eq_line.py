from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

#Vamos con llaves
#ahora desde windows

root=Tk()
root.title('Calc. Equ')
root.configure(bg="gray69")
root.geometry('350x130')  #Definir el tamaño de celda

x1label=Label(root,text="x1 = ",bg="gray69")
x1label.place(x=15,y=15)
x2label=Label(root,text="x2 = ",bg="gray69")
x2label.place(x=15,y=45)

y1label=Label(root,text="y1 = ",bg="gray69")
y1label.place(x=135,y=15)
y2label=Label(root,text="y2 = ",bg="gray69")
y2label.place(x=135,y=45)
x1=Entry(root,borderwidth=1,width=8)
x1.place(x=45,y=15)
x2=Entry(root,borderwidth=1,width=8)
x2.place(x=45,y=45)
y1=Entry(root,borderwidth=1,width=8)
y1.place(x=165,y=15)
y2=Entry(root,borderwidth=1,width=8)
y2.place(x=165,y=45)

def myclick():
    dely=float(y2.get())-float(y1.get())
    delx=float(x2.get())-float(x1.get())
    pend=round(dely/delx,2)
    const=round(float(y2.get())-pend*float(x2.get()),2)
    mylabel0 = Label(frame1, text="("+str(x1.get())+
                                  ","+str(y1.get())+") & ("+str(x2.get())+","+str(y2.get())+")",bg="gray69")
    mylabel0.pack()
    mylabel = Label(frame2, text="Y = "+str(pend)+" X + "+str(const),bg="gray69")
    mylabel.pack()
    x1a=float(x1.get())-2*abs(float(x1.get()))
    x2a=float(x2.get())+2*abs(float(x2.get()))
    x = np.linspace(float(x1a), float(x2a), 100)
    plt.plot(x, pend*x+const)
    plt.show()

mybutton=Button(root,text="Calculate",padx=20,pady=18,comman=myclick,fg="blue",bg="gray")
mybutton.place(x=230,y=10)
mylabelresp = Label(root, text="La ecuación de la recta es :",bg="gray69")
mylabelresp.place(x=20,y=70)

frame1=Frame(root,bg="gray69")
frame1.place(x=20, y=90)
frame2=Frame(root,bg="gray69")
frame2.place(x=180,y=90)
root.mainloop()