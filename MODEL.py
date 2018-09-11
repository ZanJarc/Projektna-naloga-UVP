class Voznik:
    
    def __init__(self, ime, zacetek, konec, prostor):
        self.ime = ime
        self.zacetek = zacetek
        self.konec = konec
        self.prostor = prostor
        
    def __str__(self):
        return 'To je voznik z imeonom {}, ki vozi iz {} v {} in ima v avtomobilu {} proste sedeze'.format(self.ime, self.zacetek, self.konec, self.prostor)

    def __repr__(self):
        return 'Voznik({}, {}, {}, {})'.format(self.ime, self.zacetek, self.konec, self.prostor)


class Omrezje:

    def __init__(self, slovar_grafa = None):
        if slovar_grafa == None:
            slovar = []
        self.slovar_grafa = slovar_grafa
        
        mesta = []
        for mesto in self.slovar_grafa:
            mesta.append(mesto)
        self.mesta = mesta

        povezave = []
        for mesto in self.slovar_grafa:
            for sosed in self.slovar_grafa[mesto]:
                if {sosed, mesto} not in povezave:
                    povezave.append({mesto, sosed})
        self.povezave = povezave

    def mesta(self):
        return list(slovar_grafa.keys())

    def povezave(self):
        return self.vzpostavi_povezave()

    def dodaj_mesto(self, mesto):
        if mesto not in self.slovar_grafa:
            self.slovar_grafa[mesto] = []
            self.mesta.append(mesto)

    def dodaj_povezavo(self, povezava):
        povezava = set(povezava)
        (mesto1, mesto2) = tuple(povezava)
        self.povezave.append(povezava)

        if mesto1 in self.slovar_grafa:
            self.slovar_grafa[mesto1].append(mesto2)
            self.slovar_grafa[mesto2].append(mesto1)
            
        else:
            self.slovar_grafa[mesto1] = [mesto2]
            self.slovar_grafa[mesto2].append(mesto1)


        
        

    def generiraj_povezave(self):
        
        povezave = []
        for mesto in self.slovar_grafa:
            for sosed in self.slovar_grafa[mesto]:
                if {sosed, mesto} not in povezave:
                    povezave.append({mesto, sosed})
        return povezave

    def __str__(self):
        res = "Mesta: "
        for k in self.slovar_grafa:
            res += str(k) + ", "
        res += "\nPovezave: "
        for povezava in self.generiraj_povezave():
            res += str(povezava) + " "
        return res

    def __repr__(self):
        return 'Omrezje({})'.format(self.slovar_grafa)


class Potnik:

    def __init__(self, ime, zacetek, konec):
        self.ime = ime
        self.zacetek = zacetek
        self.konec = konec


    def __str__(self):
        return 'Potnik z imenom {}, ki potuje iz {} v {}.'.format(self.ime, self.zacetek, self.konec)

    def __repr__(self):
        return 'Potnik({}, {}, {})'.format(self.ime, self.zacetek, self.konec)

def lastnosti_voznik(voznik):
        return [voznik.ime, voznik.zacetek, voznik.konec, voznik.prostor]

def lastnosti_potnik(potnik):
    return [potnik.ime, potnik.zacetek, potnik.konec]
    
def najdi_pot(omrezje, zacetek, konec, pot = None):
            if pot == None:
                pot = []
            graf = omrezje.slovar_grafa
            pot = pot + [zacetek]
            if zacetek == konec:
                return pot
            if zacetek not in graf:
                return None
            for mesto in graf[zacetek]:
                if mesto not in pot:
                    podaljsana_pot = najdi_pot(omrezje, mesto, konec, pot)
                    if podaljsana_pot: 
                        return podaljsana_pot
            return None
        
def najdi_potnikovo_pot(omrezje, potnik, pot = None):
        zacetek = potnik.zacetek
        konec = potnik.konec
        """ find a path from start_vertex to end_vertex 
            in graph """
        return najdi_pot(omrezje, zacetek, konec)

    
### ce bo celotna pot potnika "tudi" v poti voznika, ga ta lahko "pobere"

def ali_se_lahko_peljeta(omrezje, voznik, potnik):
    voznikova_pot = najdi_potnikovo_pot(omrezje, voznik)
    zacetek = potnik.zacetek
    konec = potnik.konec
    if zacetek in voznikova_pot and konec in voznikova_pot:
        if voznikova_pot.index(zacetek) < voznikova_pot.index(konec):
            if int(voznik.prostor) >= 1:
                return True
    else:
        return False
def pelje(omrezje, voznik, potnik):
        voznik.prostor = str(int(voznik.prostor) - 1)



vozniki = []
potniki = []
sortirano = {}


def prepelji(omrezje, vozniki, potniki): ### vozniki in potniki so seznam
    for voznik in vozniki:
            for potnik in potniki:
                if ali_se_lahko_peljeta(omrezje, voznik, potnik):
                    ### voznik lahko pelje potnika; mu je na poti in se nima zasedenega avtomobila
                    pelje(omrezje, voznik, potnik)
                    potniki.remove(potnik) ### ta potnik je dobil svoj prevoz
                    if voznik not in sortirano:
                        sortirano[voznik] = []
                        sortirano[voznik].append(potnik)
                    else:
                        sortirano[voznik].append(potnik)
    ### sedaj imamo voznike in potnike lepo razvrscene





