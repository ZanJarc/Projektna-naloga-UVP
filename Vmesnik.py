import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import model
okno = Tk()
okno.title('Vmesnik')

LASTNOSTI_VOZNIKI = ['Ime', 'Začetek', 'Konec', 'Prostor']
LASTNOSTI_POTNIKI = ['Ime', 'Začetek', 'Konec']
LASTNOSTI_ODGOVOR = ['Zaporedna številka', 'Stavek']

graf = {'LJUBLJANA' : ['CELJE', 'KRANJ', 'KOPER', 'NOVO MESTO'], 
'CELJE' : ['MARIBOR', 'LJUBLJANA'], 
'MARIBOR' :['CELJE', 'MURSKA SOBOTA'],
'MURSKA SOBOTA': ['MARIBOR'],
'NOVO MESTO' :['LJUBLJANA'],
'KOPER' : ['LJUBLJANA'],
'KRANJ' : ['LJUBLJANA', 'JESENICE'],
'JESENICE' : ['KRANJ']
}

omrezje = model.Omrezje(graf)
mesta = omrezje.mesta






vnos = Frame(okno ,height=400, width = 600).grid(row=0, column=0, rowspan = 4, columnspan = 6, sticky = 'W')

prostor_za_vnos_voznik = Frame(vnos)# PROSTOR ZA VNOS PODATKOV VOZNIKOV
prostor_za_vnos_voznik.grid(row=0, column=0)

prostor_za_vnos_potnik = Frame(vnos)#PROSTOR ZA VNOS PODATKOV POTNIKOV
prostor_za_vnos_potnik.grid(row=0, column=1)


prostor_za_odgovor = Frame(okno, height = 100, width = 700)
prostor_za_odgovor.grid(row = 6, column = 6, columnspan = 7,sticky = 'N')



###TUKAJ BOM NAREDIL TREEVIEW ZA ODGOVORE
treeview_odgovor = ttk.Treeview(prostor_za_odgovor)
treeview_odgovor.pack(side = 'left')
treeview_odgovor.config(height = 5)

treeview_odgovor.config(columns = LASTNOSTI_ODGOVOR)
treeview_odgovor['show'] = 'headings'
    

treeview_odgovor.column('Zaporedna številka', width = 110, anchor = 'center')
treeview_odgovor.heading('Zaporedna številka', text = 'Zaporedna številka')
treeview_odgovor.column('Stavek', width = 500, anchor = 'center')
treeview_odgovor.heading('Stavek', text = 'Stavek')
    
    


drsnik_odgovor = ttk.Scrollbar(prostor_za_odgovor, orient="vertical", command=treeview_odgovor.yview)
drsnik_odgovor.pack(side='right', fill='y')
treeview_odgovor.configure(yscrollcommand=drsnik_odgovor.set)
####


podatki_vozniki = Frame(okno, height = 200, width = 600)
podatki_vozniki.grid(row=4, column=0, rowspan=2, columnspan=6, sticky = 'W')
Label(podatki_vozniki, text = 'VOZNIKI').pack()


podatki_potniki = Frame(okno, height = 200, width = 600)
podatki_potniki.grid(row = 6, column = 0, rowspan = 2, columnspan = 6, sticky = 'W')
Label(podatki_potniki, text = 'POTNIKI').pack()

#TUKAJ BOM NAREDIL TREEVIEW ZA VOZNIKE

treeview_vozniki = ttk.Treeview(podatki_vozniki)
treeview_vozniki.pack(side = 'left')
treeview_vozniki.config(height = 3, columns = LASTNOSTI_VOZNIKI)
treeview_vozniki['show'] = 'headings'

for lastnost in LASTNOSTI_VOZNIKI:
    treeview_vozniki.column(lastnost, width = 140, anchor = 'c')
    treeview_vozniki.heading(lastnost, text = lastnost)

drsnik_vozniki = ttk.Scrollbar(podatki_vozniki, orient="vertical", command=treeview_vozniki.yview)
drsnik_vozniki.pack(side='right', fill='y')

treeview_vozniki.configure(yscrollcommand=drsnik_vozniki.set)
####

#TUKAJ BOM NAREDIL TREEVIEW ZA POTNIKE
treeview_potniki = ttk.Treeview(podatki_potniki)
treeview_potniki.pack(side = 'left')
treeview_potniki.config(height = 3, columns = LASTNOSTI_POTNIKI)
treeview_potniki['show'] = 'headings'

for lastnost in LASTNOSTI_POTNIKI:
    treeview_potniki.column(lastnost, width = 186, anchor = 'c')
    treeview_potniki.heading(lastnost, text = lastnost)

drsnik_potniki = ttk.Scrollbar(podatki_potniki, orient="vertical", command=treeview_potniki.yview)
drsnik_potniki.pack(side='right', fill='y')

treeview_potniki.configure(yscrollcommand=drsnik_potniki.set)
###








slika = ImageTk.PhotoImage(Image.open('Omrezje.gif'))
panel = Frame(okno, height=400, width = 700)
panel.grid(row=0, column=6, columnspan = 7, rowspan = 4)
prostor_za_sliko = Label(panel, image = slika).pack()


prostor_za_gumb = Frame(okno, height=200, width = 700)
prostor_za_gumb.grid(row = 4, column = 6,rowspan = 2, columnspan = 7,sticky = 'N')




prostor_za_napake = Frame(okno, height = 50, width = 700,)
prostor_za_napake.grid(row = 7, column = 6, columnspan = 7)
napaka = Label(prostor_za_napake, text = 'Tukaj se bodo izpisale napake.', fg = 'red',font='Helvetica 10 bold')
napaka.pack()


Label(prostor_za_vnos_voznik, text = 'VOZNIK').grid(row=0)
Label(prostor_za_vnos_voznik, text = 'Ime').grid(row=1, sticky='W')
Label(prostor_za_vnos_voznik, text = 'Zacetek').grid(row=2, sticky='W')
Label(prostor_za_vnos_voznik, text = 'Konec').grid(row=3, sticky='W')
Label(prostor_za_vnos_voznik, text = 'Prostor').grid(row=4, sticky='W')

vnos_voznik_ime = Entry(prostor_za_vnos_voznik, width = 21)
vnos_voznik_ime.grid(row=1, column=1)

vnos_voznik_zacetek = ttk.Combobox(prostor_za_vnos_voznik, width = 18)
vnos_voznik_zacetek['values'] = mesta
vnos_voznik_zacetek.grid(row=2, column=1)

vnos_voznik_konec = ttk.Combobox(prostor_za_vnos_voznik, width = 18)
vnos_voznik_konec['values'] = mesta

vnos_voznik_konec.grid(row=3, column=1)

vnos_voznik_prostor = Entry(prostor_za_vnos_voznik, width = 21)
vnos_voznik_prostor.grid(row=4, column=1)


def vnesi_podatke_voznik():
    if len(vnos_voznik_ime.get()) == 0:
        napaka.config(text = 'Vsak voznik potrebuje ime!')
    elif len(vnos_voznik_zacetek.get()) == 0:
        napaka.config(text ='Vsak voznik potrebuje zacetek!')
    elif len(vnos_voznik_konec.get()) == 0:
        napaka.config(text ='Vsak voznik potrebuje konec!')
    elif len(vnos_voznik_prostor.get()) == 0 or int(vnos_voznik_prostor.get()) <= 0:
        napaka.config(text ='Vsak voznik potrebuje prostor!')
    elif not vnos_voznik_prostor.get().isnumeric():
        napaka.config(text ='Vnešeni podatek pri prostoru ni številka!')
    elif vnos_voznik_konec.get() == vnos_voznik_zacetek.get():
        napaka.config(text ='Voznik ne more imeti enakega konca in zacetka!')
    else:
        voznik = model.Voznik(vnos_voznik_ime.get(), vnos_voznik_zacetek.get(), vnos_voznik_konec.get(), vnos_voznik_prostor.get())
        treeview_vozniki.insert('', 'end', values = model.lastnosti_voznik(voznik))
        model.vozniki.append(voznik)
        vnos_voznik_ime.delete(0, END), vnos_voznik_zacetek.delete(0, END), vnos_voznik_konec.delete(0, END), vnos_voznik_prostor.delete(0, END)
        napaka.config(text = 'Tukaj se bodo izpisale napake.')
    

gumb_podatki_voznik = Button(prostor_za_vnos_voznik, text = 'Vnesi podatke', command = vnesi_podatke_voznik)
gumb_podatki_voznik.grid(row = 5)


Label(prostor_za_vnos_potnik, text = 'POTNIK').grid(row=0)
Label(prostor_za_vnos_potnik, text = 'Ime').grid(row=1, sticky='W')
Label(prostor_za_vnos_potnik, text = 'Zacetek').grid(row=2, sticky='W')
Label(prostor_za_vnos_potnik, text = 'Konec').grid(row=3, sticky='W')


vnos_potnik_ime = Entry(prostor_za_vnos_potnik, width = 21)
vnos_potnik_ime.grid(row=1, column=1)

vnos_potnik_zacetek = ttk.Combobox(prostor_za_vnos_potnik, width = 18)
vnos_potnik_zacetek['values'] = mesta
vnos_potnik_zacetek.grid(row=2, column=1)

vnos_potnik_konec = ttk.Combobox(prostor_za_vnos_potnik, width = 18)
vnos_potnik_konec['values'] = mesta
vnos_potnik_konec.grid(row=3, column=1)



def vnesi_podatke_potnik():
    if len(vnos_potnik_ime.get()) == 0:
        napaka.config(text = 'Vsak potnik potrebuje ime!')
    elif len(vnos_potnik_zacetek.get()) == 0:
        napaka.config(text = 'Vsak potnik potrebuje zacetek!')
    elif len(vnos_potnik_konec.get()) == 0:
        napaka.config(text = 'Vsak potnik potrebuje konec!')
    elif vnos_potnik_konec.get() == vnos_potnik_zacetek.get():
        napaka.config(text = 'Potnik ne more imeti enakega konca in zacetka!')
    else:
        potnik = model.Potnik(vnos_potnik_ime.get(), vnos_potnik_zacetek.get(), vnos_potnik_konec.get())
        treeview_potniki.insert('', 'end', values = model.lastnosti_potnik(potnik))
        model.potniki.append(potnik)
        vnos_potnik_ime.delete(0, END), vnos_potnik_zacetek.delete(0, END), vnos_potnik_konec.delete(0, END)
        napaka.config(text = 'Tukaj se bodo izpisale napake.')
    
    

gumb_podatki_potnik = Button(prostor_za_vnos_potnik, text = 'Vnesi podatke', command = vnesi_podatke_potnik)
gumb_podatki_potnik.grid(row = 4)







def simulacija(): #WHERE THE MAGIC HAPPENS
    treeview_odgovor.delete(*treeview_odgovor.get_children())
    i = 1
    if model.vozniki == [] and model.potniki == []:
        napaka.config(text = 'Prosim vstavite podatke!')
    else:
        napaka.config(text = 'Tukaj se bodo izpisale napake.')
        model.prepelji(omrezje, model.vozniki, model.potniki) ###v modelu se lepo vse sortira
        odgovor = ''
        for voznik in model.vozniki:
            if voznik not in model.sortirano: ###to pomeni, da na poti ne pobere nikogar
                odgovor += '{} se pelje sam.'.format(voznik.ime)
                print(odgovor)
                treeview_odgovor.insert('', 'end', values = (i, odgovor))
                odgovor = ''
                i+=1
            else:
                odgovor += '{} pelje'.format(voznik.ime)
                for potnik in model.sortirano[voznik]:
                      odgovor += ' {}, '.format(potnik.ime)

                odgovor = odgovor[:-2]
                odgovor += '.'
                treeview_odgovor.insert('', 'end', values = (i, odgovor))
                print(odgovor)
                odgovor = ''
                i+=1
                                        
                
        for potnik in model.potniki: ## tukaj ostanejo tisti, ki ne dobijo prevoza
            odgovor +='{} ni dobil prevoza.\n'.format(potnik.ime)
            treeview_odgovor.insert('', 'end', values = (i, odgovor))
            odgovor = ''
            i += 1
                
    
        

glavni_gumb = Button(prostor_za_gumb, text = 'ZAŽENI SIMULACIJO', command = simulacija, font = 'Helvetica 10 bold')
glavni_gumb.grid(row = 0)

def zbrisi():
    model.potniki.clear()
    model.vozniki.clear()
    model.sortirano.clear
    treeview_vozniki.delete(*treeview_vozniki.get_children())
    treeview_potniki.delete(*treeview_potniki.get_children())
    treeview_odgovor.delete(*treeview_odgovor.get_children())
    odgovor = ''
    napaka.config(text = 'Tukaj se bodo izpisale napake.')
    
gumb_zbrisi = Button(prostor_za_gumb, text = 'Zbriši vse podatke', command = zbrisi)
gumb_zbrisi.grid(row=0, column = 1)




okno.mainloop()

