from tkinter import *
from tkinter.messagebox import *


Tunniplaan = Tk()
Tunniplaan.title("Tunniplaan")
Tunniplaan.geometry("1013x610")

def read_file():
    tund_r={}
    file=open("tunnid.txt","r")
    for line in file:
        tund,kirjeldus=line.strip().split(":")
        tund_r[tund.strip()]=kirjeldus.strip()
    file.close()
    print(tund_r)
    return tund_r

def window_text(t:str):
    if (askyesno("Küsimus","Kas tahad kirjeldust näha?")):
        alam_aken=Toplevel()
        alam_aken.geometry("510x130")
        lbl_r=Label(alam_aken, text=tund_r[t], font="Arial 30").grid(row=1, column=0)
        c=Canvas(alam_aken, height=500, width=500)
        file=PhotoImage(file="amogus.gif")
        c.create_image(10,10,image=file,anchor=NW)
        c.grid(row=2, column=1)
        #command=lambda:window_text("amogus.gif")
        alam_aken.mainloop()
    else:
        showinfo("Vatus","Kui ei taha, siis ei taha!")

tund_r=read_file()

Probel=Label(Tunniplaan, text=" ", height=2, width=9, font="Arial 20", bg="white", relief="groove").grid(row=0, column=0)


# ESMASPÄEV

l2=Label(Tunniplaan, text="Esmaspäev", height=3, width=9, font="Arial 20", fg="#000000", bg="white", relief="groove").grid(row=1, column=0, rowspan=2, sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=1, column=1,rowspan=2,sticky=N+S+W+E)

Mul=Button(Tunniplaan, text="Multimeedia", height=2, width=3, font="Arial 12",fg="#000000", bg="#9370DB", relief="groove", command=lambda:window_text("amogus.gif Multimeedia", )).grid(row=1, column=2,columnspan=2,sticky=N+S+W+E )
Prog=Button(Tunniplaan, text="Programmeerimise alused", height=2, width=6, font="Arial 12",fg="#000000", bg="#87CEEB", relief="groove",command=lambda:window_text("Programmeerimise alused")).grid(row=2, column=2,columnspan=3,sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 12",fg="#000000", bg="white", relief="groove").grid(row=1, column=4,sticky=N+S+W+E)
Prog=Button(Tunniplaan, text="Programmeerimise alused", height=2, width=6, font="Arial 12",fg="#000000", bg="#87CEEB", relief="groove",command=lambda:window_text("Programmeerimise alused")).grid(row=1, column=5,columnspan=3,sticky=N+S+W+E)
Mul=Button(Tunniplaan, text="Multimeedia", height=2, width=3, font="Arial 12",fg="#000000", bg="#9370DB", relief="groove",command=lambda:window_text("Multimeedia")).grid(row=2, column=5,columnspan=2,sticky=N+S+W+E )
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 12",fg="#000000", bg="white", relief="groove").grid(row=2, column=7,sticky=N+S+W+E)
Ruh=Button(Tunniplaan, text="Rühmajuhataja \n tund", height=2, width=6, font="Arial 8",fg="#000000", bg="#87CEEB", relief="groove",command=lambda:window_text("Ruhmajuhataja tund")).grid(row=1, column=8,rowspan=2, columnspan=1,sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 12",fg="#000000", bg="white", relief="groove").grid(row=1, column=9,rowspan=2, columnspan=2,sticky=N+S+W+E)


# TEISIPÄEV
l2=Label(Tunniplaan, text="Teisipäev", height=3, width=9, font="Arial 20", fg="#000000", bg="white", relief="groove").grid(row=3, column=0, rowspan=2, sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=3, column=1,rowspan=2,sticky=N+S+W+E )

Eng1=Button(Tunniplaan, text="Inglise keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#FFF8DC", relief="groove",command=lambda:window_text("Inglise keel1")).grid(row=3, column=2,columnspan=2 ,sticky=N+S+W+E)
Eng2=Button(Tunniplaan, text="Inglise keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#BA55D3", relief="groove",command=lambda:window_text("Inglise keel2")).grid(row=4, column=2,columnspan=2 ,sticky=N+S+W+E)
Oper=Button(Tunniplaan, text="Operatsioonisüsteemide alused", height=2, width=6, font="Arial 8",fg="#000000", bg="#9932CC", relief="groove",command=lambda:window_text("Operatsioonisusteemide alused")).grid(row=3, column=4,rowspan=2,columnspan=2 ,sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 8",fg="#000000", bg="white", relief="groove").grid(row=3, column=6,rowspan=2,columnspan=1 ,sticky=N+S+W+E)
Keh=Button(Tunniplaan, text="Kehaline kasvatus", height=2, width=6, font="Arial 8",fg="#000000", bg="#CD5C5C", relief="groove",command=lambda:window_text("Kehaline Kasvatus")).grid(row=3, column=7,rowspan=2,columnspan=2 ,sticky=N+S+W+E)
Est1=Button(Tunniplaan, text="Eesti keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#9999FF", relief="groove",command=lambda:window_text("Eesti keel1")).grid(row=3, column=9,columnspan=1 ,sticky=N+S+W+E)
Est2=Button(Tunniplaan, text="Eesti keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#808080", relief="groove",command=lambda:window_text("Eesti keel2")).grid(row=4, column=9,columnspan=1 ,sticky=N+S+W+E)
Aja=Button(Tunniplaan, text="Ajalugu, \n Inimgeograafia \n Inimeseõpetus", height=2, width=6, font="Arial 8",fg="#000000", bg="#FFFFCC", relief="groove",command=lambda:window_text("Ajalugu, inimgeograafia")).grid(row=3, column=10,rowspan=2,columnspan=1 ,sticky=N+S+W+E)



# KOLMAPÄEV
l4=Label(Tunniplaan, text="Kolmapäev", height=3, width=9, font="Arial 20", fg="#000000", bg="white", relief="groove").grid(row=5, column=0, rowspan=2, sticky=N+S+W+E)
l9=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=5, column=1,rowspan=2,sticky=N+S+W+E )

Prog=Button(Tunniplaan, text="Programmeerimise alused", height=2, width=6, font="Arial 12",fg="#000000", bg="#87CEEB", relief="groove",command=lambda:window_text("Programmeerimise alused")).grid(row=5, column=2,columnspan=3,sticky=N+S+W+E)
Mul=Button(Tunniplaan, text="Multimeedia", height=2, width=3, font="Arial 12",fg="#000000", bg="#9370DB", relief="groove",command=lambda:window_text("Multimeedia")).grid(row=6, column=2,columnspan=3,sticky=N+S+W+E )
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 8",fg="#000000", bg="white", relief="groove").grid(row=5, column=5,rowspan=2,columnspan=1 ,sticky=N+S+W+E)
Mul=Button(Tunniplaan, text="Multimeedia", height=2, width=3, font="Arial 12",fg="#000000", bg="#9370DB", relief="groove",command=lambda:window_text("Multimeedia")).grid(row=5, column=6,columnspan=3,sticky=N+S+W+E )
Prog=Button(Tunniplaan, text="Programmeerimise alused", height=2, width=6, font="Arial 12",fg="#000000", bg="#87CEEB", relief="groove",command=lambda:window_text("Programmeerimise alused")).grid(row=6, column=6,columnspan=3,sticky=N+S+W+E)
Kun=Button(Tunniplaan, text="Kunstiained", height=2, width=6, font="Arial 8",fg="#000000", bg="#DA70D6", relief="groove",command=lambda:window_text("Kunstiained")).grid(row=5, column=9,rowspan=2,columnspan=2 ,sticky=N+S+W+E)


# NELJAPÄEV
l5=Label(Tunniplaan, text="Neljapäev", height=3, width=9, font="Arial 20", fg="#000000", bg="white", relief="groove").grid(row=7, column=0, rowspan=2, sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=7, column=1,rowspan=2,sticky=N+S+W+E )

And=Button(Tunniplaan, text="Andmebasidesüsteemide \n alused", height=2, width=6, font="Arial 8",fg="#000000", bg="#DC143C", relief="groove",command=lambda:window_text("Andmebaasisusteemide alused")).grid(row=7, column=2,rowspan=2,columnspan=2 ,sticky=N+S+W+E)
And=Button(Tunniplaan, text="Andmebasidesüsteemide \n alused", height=2, width=6, font="Arial 8",fg="#000000", bg="#DC143C", relief="groove",command=lambda:window_text("Andmebaasisusteemide alused")).grid(row=7, column=4,rowspan=2,columnspan=3 ,sticky=N+S+W+E)
Aja=Button(Tunniplaan, text="Ajalugu, \n Inimgeograafia \n Inimeseõpetus", height=2, width=6, font="Arial 8",fg="#000000", bg="#FFFFCC", relief="groove",command=lambda:window_text("Ajalugu, inimgeograafia")).grid(row=7, column=8,rowspan=2,columnspan=1 ,sticky=N+S+W+E)
Probel=Button(Tunniplaan, text=" ", height=2, width=6, font="Arial 8",fg="#000000", bg="white", relief="groove").grid(row=7, column=7,rowspan=2,columnspan=1 ,sticky=N+S+W+E)
Est1=Button(Tunniplaan, text="Eesti keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#9999FF", relief="groove",command=lambda:window_text("Eesti keel1")).grid(row=7, column=9,columnspan=1 ,sticky=N+S+W+E)
Est2=Button(Tunniplaan, text="Eesti keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#808080", relief="groove",command=lambda:window_text("Eesti keel2")).grid(row=8, column=9,columnspan=1 ,sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 8",fg="#000000", bg="white", relief="groove").grid(row=7, column=10,rowspan=2,columnspan=1 ,sticky=N+S+W+E)




# REEDE
l6=Label(Tunniplaan, text="Reede", height=3, width=9, font="Arial 20", fg="#000000", bg="white", relief="groove").grid(row=9, column=0, rowspan=2, sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=9, column=1,rowspan=2,sticky=N+S+W+E )
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=9, column=2,rowspan=2,sticky=N+S+W+E )

Ven=Button(Tunniplaan, text="Keel ja kirjandus", height=2, width=6, font="Arial 8",fg="#000000", bg="#9ACD32", relief="groove",command=lambda:window_text("Keel ja kirjandus")).grid(row=9, column=3,rowspan=2,columnspan=2 ,sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=9, column=5,rowspan=2,sticky=N+S+W+E )
Mat=Button(Tunniplaan, text="Matemaatika", height=2, width=3, font="Arial 12",fg="#000000", bg="#F08080", relief="groove",command=lambda:window_text("Matemaatika")).grid(row=9, column=6,rowspan=2,columnspan=2,sticky=N+S+W+E )
Suh=Button(Tunniplaan, text="Suhtlemine ja \n klienditeenindus", height=2, width=3, font="Arial 8",fg="#000000", bg="#9370DB", relief="groove",command=lambda:window_text("Suhtlemine ja klienditeenindus")).grid(row=9, column=8,rowspan=2,columnspan=2,sticky=N+S+W+E )
Aja=Button(Tunniplaan, text="Ajalugu, \n Inimgeograafia \n Inimeseõpetus", height=2, width=6, font="Arial 8",fg="#000000", bg="#FFFFCC", relief="groove",command=lambda:window_text("Ajalugu, inimgeograafia")).grid(row=9, column=10,rowspan=2,columnspan=1 ,sticky=N+S+W+E)




#p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev", "Reede"]
#j=0

#for i in range(1,10,2):
#    Ep=Label(Tunniplaan, text=p[j],relief="solid").grid(row=i,column=0,rowspan=2,sticky=N+S+W+E)
#    j+=1

#p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev", "Reede"]
#j=0


#for i in range(1,10,2):
#    Ep=Label(Tunniplaan, text=p[j],relief="groove",bg="white").grid(row=i,column=0,rowspan=2,sticky=N+S+W+E)
#    j+=1

#kell=["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12,40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]



t0=Label(Tunniplaan, text="0", height=2, width=5, font="Arial 20",fg="#000000", bg="white", relief="groove").grid(row=0, column=1, sticky=N+S+W+E)

t1=Label(Tunniplaan, text="1", height=2, width=5, font="Arial 20",fg="#000000", bg="white", relief="groove").grid(row=0, column=2, sticky=N+S+W+E)

t2=Label(Tunniplaan, text="2", height=2, width=5, font="Arial 20",fg="#000000", bg="white", relief="groove").grid(row=0, column=3, sticky=N+S+W+E)

t3=Label(Tunniplaan, text="3", height=2, width=5, font="Arial 20",fg="#000000", bg="white", relief="groove").grid(row=0, column=4, sticky=N+S+W+E)

t4=Label(Tunniplaan, text="4", height=2, width=5, font="Arial 20",fg="#000000", bg="white", relief="groove").grid(row=0, column=5, sticky=N+S+W+E)

t5=Label(Tunniplaan, text="5", height=2, width=5, font="Arial 20",fg="#000000", bg="white", relief="groove").grid(row=0, column=6, sticky=N+S+W+E)

t6=Label(Tunniplaan, text="6", height=2, width=5, font="Arial 20",fg="#000000", bg="white", relief="groove").grid(row=0, column=7, sticky=N+S+W+E)

t7=Label(Tunniplaan, text="7", height=2, width=5, font="Arial 20",fg="#000000", bg="white", relief="groove").grid(row=0, column=8, sticky=N+S+W+E)

t8=Label(Tunniplaan, text="8", height=2, width=5, font="Arial 20",fg="#000000", bg="white", relief="groove").grid(row=0, column=9, sticky=N+S+W+E)

t9=Label(Tunniplaan, text="9", height=2, width=5, font="Arial 20",fg="#000000", bg="white", relief="groove").grid(row=0, column=10, sticky=N+S+W+E)


Tunniplaan.mainloop()
