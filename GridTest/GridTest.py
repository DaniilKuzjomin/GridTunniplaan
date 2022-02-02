from tkinter import *

Tunniplaan = Tk()
Tunniplaan.title("Tunniplaan")
Tunniplaan.geometry("1010x650")


Probel=Label(Tunniplaan, text=" ", height=2, width=9, font="Arial 20", bg="white", relief="groove").grid(row=0, column=0)


# ESMASPÄEV

l2=Label(Tunniplaan, text="Esmaspäev", height=3, width=9, font="Arial 20", fg="#000000", bg="white", relief="groove").grid(row=1, column=0, rowspan=2, sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=1, column=1,rowspan=2,sticky=N+S+W+E)

Mul=Label(Tunniplaan, text="Multimeedia", height=2, width=3, font="Arial 12",fg="#000000", bg="#9370DB", relief="groove").grid(row=1, column=2,columnspan=2,sticky=N+S+W+E )
Prog=Label(Tunniplaan, text="Programmeerimise alused", height=2, width=6, font="Arial 12",fg="#000000", bg="#87CEEB", relief="groove").grid(row=2, column=2,columnspan=3,sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 12",fg="#000000", bg="white", relief="groove").grid(row=1, column=4,sticky=N+S+W+E)
Prog=Label(Tunniplaan, text="Programmeerimise alused", height=2, width=6, font="Arial 12",fg="#000000", bg="#87CEEB", relief="groove").grid(row=1, column=5,columnspan=3,sticky=N+S+W+E)
Mul=Label(Tunniplaan, text="Multimeedia", height=2, width=3, font="Arial 12",fg="#000000", bg="#9370DB", relief="groove").grid(row=2, column=5,columnspan=2,sticky=N+S+W+E )
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 12",fg="#000000", bg="white", relief="groove").grid(row=2, column=7,sticky=N+S+W+E)
Ruh=Label(Tunniplaan, text="Rühmajuhataja \n tund", height=2, width=6, font="Arial 8",fg="#000000", bg="#87CEEB", relief="groove").grid(row=1, column=8,rowspan=2, columnspan=1,sticky=N+S+W+E)



# TEISIPÄEV
l2=Label(Tunniplaan, text="Teisipäev", height=3, width=9, font="Arial 20", fg="#000000", bg="white", relief="groove").grid(row=3, column=0, rowspan=2, sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=3, column=1,rowspan=2,sticky=N+S+W+E )

Eng1=Label(Tunniplaan, text="Inglise keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#FFF8DC", relief="groove").grid(row=3, column=2,columnspan=2 ,sticky=N+S+W+E)
Eng2=Label(Tunniplaan, text="Inglise keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#BA55D3", relief="groove").grid(row=4, column=2,columnspan=2 ,sticky=N+S+W+E)
Oper=Label(Tunniplaan, text="Operatsioonisüsteemide alused", height=2, width=6, font="Arial 8",fg="#000000", bg="#9932CC", relief="groove").grid(row=3, column=4,rowspan=2,columnspan=2 ,sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 8",fg="#000000", bg="white", relief="groove").grid(row=3, column=6,rowspan=2,columnspan=1 ,sticky=N+S+W+E)
Keh=Label(Tunniplaan, text="Kehaline kasvatus", height=2, width=6, font="Arial 8",fg="#000000", bg="#CD5C5C", relief="groove").grid(row=3, column=7,rowspan=2,columnspan=2 ,sticky=N+S+W+E)
Est1=Label(Tunniplaan, text="Eesti keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#9999FF", relief="groove").grid(row=3, column=9,columnspan=1 ,sticky=N+S+W+E)
Est2=Label(Tunniplaan, text="Eesti keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#808080", relief="groove").grid(row=4, column=9,columnspan=1 ,sticky=N+S+W+E)
Aja=Label(Tunniplaan, text="Ajalugu, \n Inimgeograafia \n Inimeseõpetus", height=2, width=6, font="Arial 8",fg="#000000", bg="#FFFFCC", relief="groove").grid(row=3, column=10,rowspan=2,columnspan=1 ,sticky=N+S+W+E)



# KOLMAPÄEV
l4=Label(Tunniplaan, text="Kolmapäev", height=3, width=9, font="Arial 20", fg="#000000", bg="white", relief="groove").grid(row=5, column=0, rowspan=2, sticky=N+S+W+E)
l9=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=5, column=1,rowspan=2,sticky=N+S+W+E )

Prog=Label(Tunniplaan, text="Programmeerimise alused", height=2, width=6, font="Arial 12",fg="#000000", bg="#87CEEB", relief="groove").grid(row=5, column=2,columnspan=3,sticky=N+S+W+E)
Mul=Label(Tunniplaan, text="Multimeedia", height=2, width=3, font="Arial 12",fg="#000000", bg="#9370DB", relief="groove").grid(row=6, column=2,columnspan=3,sticky=N+S+W+E )
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 8",fg="#000000", bg="white", relief="groove").grid(row=5, column=5,rowspan=2,columnspan=1 ,sticky=N+S+W+E)
Mul=Label(Tunniplaan, text="Multimeedia", height=2, width=3, font="Arial 12",fg="#000000", bg="#9370DB", relief="groove").grid(row=5, column=6,columnspan=3,sticky=N+S+W+E )
Prog=Label(Tunniplaan, text="Programmeerimise alused", height=2, width=6, font="Arial 12",fg="#000000", bg="#87CEEB", relief="groove").grid(row=6, column=6,columnspan=3,sticky=N+S+W+E)
Kun=Label(Tunniplaan, text="Kunstiained", height=2, width=6, font="Arial 8",fg="#000000", bg="#DA70D6", relief="groove").grid(row=5, column=9,rowspan=2,columnspan=2 ,sticky=N+S+W+E)


# NELJAPÄEV
l5=Label(Tunniplaan, text="Neljapäev", height=3, width=9, font="Arial 20", fg="#000000", bg="white", relief="groove").grid(row=7, column=0, rowspan=2, sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=7, column=1,rowspan=2,sticky=N+S+W+E )

And=Label(Tunniplaan, text="Andmebasidesüsteemide \n alused", height=2, width=6, font="Arial 8",fg="#000000", bg="#DC143C", relief="groove").grid(row=7, column=2,rowspan=2,columnspan=2 ,sticky=N+S+W+E)
And=Label(Tunniplaan, text="Andmebasidesüsteemide \n alused", height=2, width=6, font="Arial 8",fg="#000000", bg="#DC143C", relief="groove").grid(row=7, column=4,rowspan=2,columnspan=3 ,sticky=N+S+W+E)
Aja=Label(Tunniplaan, text="Ajalugu, \n Inimgeograafia \n Inimeseõpetus", height=2, width=6, font="Arial 8",fg="#000000", bg="#FFFFCC", relief="groove").grid(row=7, column=7,rowspan=2,columnspan=1 ,sticky=N+S+W+E)
Est1=Label(Tunniplaan, text="Eesti keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#9999FF", relief="groove").grid(row=7, column=9,columnspan=1 ,sticky=N+S+W+E)
Est2=Label(Tunniplaan, text="Eesti keel", height=2, width=6, font="Arial 12",fg="#000000", bg="#808080", relief="groove").grid(row=8, column=9,columnspan=1 ,sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 8",fg="#000000", bg="white", relief="groove").grid(row=7, column=10,rowspan=2,columnspan=1 ,sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=2, width=6, font="Arial 8",fg="#000000", bg="white", relief="groove").grid(row=7, column=11,rowspan=2,columnspan=1 ,sticky=N+S+W+E)




# REEDE
l6=Label(Tunniplaan, text="Reede", height=3, width=9, font="Arial 20", fg="#000000", bg="white", relief="groove").grid(row=9, column=0, rowspan=2, sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=9, column=1,rowspan=2,sticky=N+S+W+E )
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=9, column=2,rowspan=2,sticky=N+S+W+E )

Ven=Label(Tunniplaan, text="Keel ja kirjandus", height=2, width=6, font="Arial 8",fg="#000000", bg="#9ACD32", relief="groove").grid(row=9, column=3,rowspan=2,columnspan=2 ,sticky=N+S+W+E)
Probel=Label(Tunniplaan, text=" ", height=3, width=5, font="Arial 20", bg="white", relief="groove").grid(row=9, column=5,rowspan=2,sticky=N+S+W+E )
Mat=Label(Tunniplaan, text="Matemaatika", height=2, width=3, font="Arial 12",fg="#000000", bg="#F08080", relief="groove").grid(row=9, column=6,rowspan=2,columnspan=2,sticky=N+S+W+E )
Suh=Label(Tunniplaan, text="Suhtlemine ja \n klienditeenindus", height=2, width=3, font="Arial 8",fg="#000000", bg="#9370DB", relief="groove").grid(row=9, column=8,rowspan=2,columnspan=2,sticky=N+S+W+E )
Aja=Label(Tunniplaan, text="Ajalugu, \n Inimgeograafia \n Inimeseõpetus", height=2, width=6, font="Arial 8",fg="#000000", bg="#FFFFCC", relief="groove").grid(row=9, column=10,rowspan=2,columnspan=1 ,sticky=N+S+W+E)




# Номер Урока
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
