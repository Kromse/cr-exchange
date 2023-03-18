from forex_python.converter import CurrencyRates
from time import sleep
from tkinter import *

root = Tk()
root.title("Valutaomregner")
root.geometry("200x200")

cr = CurrencyRates()



#l1 og e er mængde

label1 = Label(root, text="Mængde: ")
label1.grid(row=1)

mængde = Entry(root, borderwidth=2,)
mængde.grid(row=1, column=2)

#l2 og e1 er valuta fra

label2 = Label(root, borderwidth=2, text="Fra: ")
label2.grid(row=3,)

fra_valuta = Entry(root, borderwidth=2)
fra_valuta.grid(row=3, column=2)

#l3 og e2 er valuta til

label3 = Label(root, borderwidth=2, text="Til: ")
label3.grid(row=5)

til_valuta = Entry(root, borderwidth=2)
til_valuta.grid(row=5, column=2)


def udregn():
        sum1 = mængde.get()
        sum2 = fra_valuta.get()
        sum3 = til_valuta.get()
        resultat = cr.convert(sum2, sum3, sum1)
        label5.config(text=resultat)

    

#b1 er vores knap

b1 = Button(root, borderwidth=2, height=2, width=8, text="Omregn", command=udregn)
b1.grid(row=7, column=2)

#4 og l5 er vores resultat

label4 = Label(root, borderwidth=2, text="Resultat: ")
label4.grid(row=9,)

label5 = Label(root, borderwidth=2, text="")
label5.grid(row=9, column=1)


##cr = CurrencyRates()

##mængde = int(input("Angiv mængde du vil omregne: "))

#fra_valuta = input("Angiv hvilken valuta du vil omregne fra: ").upper()

#til_valuta = input("Angiv hvilken valuta du vil omregne til: ").upper()

#print("Du omregner", mængde, fra_valuta, "til", til_valuta,".")

#resultat = cr.convert(fra_valuta, til_valuta, mængde)

#print("", resultat)






root.mainloop()