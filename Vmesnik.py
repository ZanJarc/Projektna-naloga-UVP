import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import MODEL
okno = Tk()
okno.title('Vmesnik')

LASTNOSTI_VOZNIKI = ['Ime', 'Začetek', 'Konec', 'Prostor']
LASTNOSTI_POTNIKI = ['Ime', 'Začetek', 'Konec']

graf = {'LJUBLJANA' : ['CELJE', 'KRANJ', 'KOPER', 'NOVO MESTO'], 
'CELJE' : ['MARIBOR', 'LJUBLJANA'], 
'MARIBOR' :['CELJE', 'MURSKA SOBOTA'],
'MURSKA SOBOTA': ['MARIBOR'],
'NOVO MESTO' :['LJUBLJANA'],
'KOPER' : ['LJUBLJANA'],
'KRANJ' : ['LJUBLJANA', 'JESENICE'],
'JESENICE' : ['KRANJ']
}

Omrezje = MODEL.Omrezje(graf)
Mesta = Omrezje.mesta


VOZNIKI = []
POTNIKI = []

SORTIRANO = {}



VNOS = Frame(okno ,height=400, width = 600).grid(row=0, column=0, rowspan = 4, columnspan = 6, sticky = 'W')

prostor_za_vnos_voznik = Frame(VNOS)# PROSTOR ZA VNOS PODATKOV VOZNIKOV
prostor_za_vnos_voznik.grid(row=0, column=0)

prostor_za_vnos_potnik = Frame(VNOS)#PROSTOR ZA VNOS PODATKOV POTNIKOV
prostor_za_vnos_potnik.grid(row=0, column=1)


prostor_za_podatke = Frame(okno, bg = 'orange', height=400, width = 600)# PROSTOR ZA IZPIS ŽE VNESENIH PODATKOV
prostor_za_podatke.grid(row=4, column=0, rowspan = 4, columnspan = 6, sticky = 'W')
#stanje_vozniki = Frame(prostor_za_podatke).grid(row=0)




slika = ImageTk.PhotoImage(Image.open('Omrezje.gif'))
panel = Frame(okno, height=400, width = 700)
panel.grid(row=0, column=6, columnspan = 7, rowspan = 4)
prostor_za_sliko = Label(panel, image = slika).pack()


prostor_za_gumb = Frame(okno, height=200, width = 700, bg = 'green')
prostor_za_gumb.grid(row = 4, column = 6,rowspan = 2, columnspan = 7,sticky = 'N')


prostor_za_odgovor = Frame(okno, height = 100, width = 700, bg = 'blue')
prostor_za_odgovor.grid(row = 6, column = 6, columnspan = 7,sticky = 'N')


prostor_za_napake = Frame(okno, height = 50, width = 700, bg = 'red')
prostor_za_napake.grid(row = 7, column = 6, columnspan = 7)


Label(prostor_za_vnos_voznik, text = 'VOZNIK').grid(row=0)
Label(prostor_za_vnos_voznik, text = 'Ime').grid(row=1, sticky='W')
Label(prostor_za_vnos_voznik, text = 'Zacetek').grid(row=2, sticky='W')
Label(prostor_za_vnos_voznik, text = 'Konec').grid(row=3, sticky='W')
Label(prostor_za_vnos_voznik, text = 'Prostor').grid(row=4, sticky='W')

vnos_voznik_ime = Entry(prostor_za_vnos_voznik, width = 21)
vnos_voznik_ime.grid(row=1, column=1)

vnos_voznik_zacetek = ttk.Combobox(prostor_za_vnos_voznik, width = 18)
vnos_voznik_zacetek['values'] = Mesta
vnos_voznik_zacetek.grid(row=2, column=1)

vnos_voznik_konec = ttk.Combobox(prostor_za_vnos_voznik, width = 18)
vnos_voznik_konec['values'] = Mesta

vnos_voznik_konec.grid(row=3, column=1)

vnos_voznik_prostor = Entry(prostor_za_vnos_voznik, width = 21)
vnos_voznik_prostor.grid(row=4, column=1)


def vnesi_podatke_voznik():
    if len(vnos_voznik_ime.get()) == 0:
        raise ValueError('Vsak voznik potrebuje ime!')
    elif len(vnos_voznik_zacetek.get()) == 0:
        raise ValueError('Vsak voznik potrebuje zacetek!')
    elif len(vnos_voznik_konec.get()) == 0:
        raise ValueError('Vsak voznik potrebuje konec!')
    elif len(vnos_voznik_prostor.get()) == 0 or int(vnos_voznik_prostor.get()) <= 0:
        raise ValueError('Vsak voznik potrebuje prostor!')
    elif not vnos_voznik_prostor.get().isnumeric():
        raise ValueError('Vnešeni podatek pri prostoru ni številka!')
    elif vnos_voznik_konec.get() == vnos_voznik_zacetek.get():
        raise ValueError('Voznik ne more imeti enakega konca in zacetka!')
    else:
        driver = MODEL.Voznik(vnos_voznik_ime.get(), vnos_voznik_zacetek.get(), vnos_voznik_konec.get(), vnos_voznik_prostor.get())
        VOZNIKI.append(driver)
        vnos_voznik_ime.delete(0, END), vnos_voznik_zacetek.delete(0, END), vnos_voznik_konec.delete(0, END), vnos_voznik_prostor.delete(0, END)
   
    

gumb_podatki_voznik = Button(prostor_za_vnos_voznik, text = 'Vnesi podatke', command = vnesi_podatke_voznik)
gumb_podatki_voznik.grid(row = 4)


Label(prostor_za_vnos_potnik, text = 'POTNIK').grid(row=0)
Label(prostor_za_vnos_potnik, text = 'Ime').grid(row=1, sticky='W')
Label(prostor_za_vnos_potnik, text = 'Zacetek').grid(row=2, sticky='W')
Label(prostor_za_vnos_potnik, text = 'Konec').grid(row=3, sticky='W')


vnos_potnik_ime = Entry(prostor_za_vnos_potnik, width = 21)
vnos_potnik_ime.grid(row=1, column=1)

vnos_potnik_zacetek = ttk.Combobox(prostor_za_vnos_potnik, width = 18)
vnos_potnik_zacetek['values'] = Mesta
vnos_potnik_zacetek.grid(row=2, column=1)

vnos_potnik_konec = ttk.Combobox(prostor_za_vnos_potnik, width = 18)
vnos_potnik_konec['values'] = Mesta
vnos_potnik_konec.grid(row=3, column=1)



def vnesi_podatke_potnik():
    if len(vnos_potnik_ime.get()) == 0:
        raise ValueError('Vsak potnik potrebuje ime!')
    elif len(vnos_potnik_zacetek.get()) == 0:
        raise ValueError('Vsak potnik potrebuje zacetek!')
    elif len(vnos_potnik_konec.get()) == 0:
        raise ValueError('Vsak potnik potrebuje konec!')
    elif vnos_potnik_konec.get() == vnos_potnik_zacetek.get():
        raise ValueError('Potnik ne more imeti enakega konca in zacetka!')
    else:
        passenger = MODEL.Potnik(vnos_potnik_ime.get(), vnos_potnik_zacetek.get(), vnos_potnik_konec.get())
        POTNIKI.append(passenger)
        vnos_potnik_ime.delete(0, END), vnos_potnik_zacetek.delete(0, END), vnos_potnik_konec.delete(0, END)

    
    

gumb_podatki_potnik = Button(prostor_za_vnos_potnik, text = 'Vnesi podatke', command = vnesi_podatke_potnik)
gumb_podatki_potnik.grid(row = 4)




prostor_podatkov_voznikov = Label(prostor_za_podatke)
prostor_podatkov_voznikov.pack()

prostor_podatkov_potnikov = Label(prostor_za_podatke)
prostor_podatkov_potnikov.pack()

imena_potniki = []
def simulacija(): #WHERE THE MAGIC HAPPENS
    for voznik in VOZNIKI:
        for potnik in POTNIKI:
            if MODEL.ali_se_lahko_peljeta(Omrezje, voznik, potnik):
                ### voznik lahko pelje potnika; mu je na poti in se nima zasedenega avtomobila
                MODEL.pelje(Omrezje, voznik, potnik)
                POTNIKI.remove(potnik) ### ta potnik je dobil svoj prevoz
                if voznik not in SORTIRANO:
                    SORTIRANO[voznik] = []
                    SORTIRANO[voznik].append(potnik)
                else:
                    SORTIRANO[voznik].append(potnik)
    for voznik in VOZNIKI:
        if voznik not in SORTIRANO: ###to pomeni, da na poti ne pobere nikogar
            print('{} se pelje sam'.format(voznik.ime))
        else:
            tekst = '{} pelje'.format(voznik.ime)
            for potnik in SORTIRANO[voznik]:
                  tekst += ' {}, '.format(potnik.ime)

            tekst = tekst[:-2]
            tekst += '.'
            print(tekst)
    for potnik in POTNIKI: ## tukaj ostanejo tisti, ki ne dobijo prevoza
        print('{} ni dobil prevoza'.format(potnik.ime))
                
    
        

GLAVNI_GUMB = Button(prostor_za_gumb, text = 'Zaženi simulacijo', command = simulacija)
GLAVNI_GUMB.grid(row = 0)

def zbrisi():
    POTNIKI = VOZNIKI = []
    
gumb_zbrisi = Button(prostor_za_gumb, text = 'Zbriši vse podatke', command = zbrisi)
gumb_zbrisi.grid(row=0, column = 1)




okno.mainloop()

