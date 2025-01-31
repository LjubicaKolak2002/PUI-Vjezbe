from spil import Spil
from igrac import Igrac
from human import Human

class StanjeIgraca:
    def __init__(self, igrac):
        self.igrac = igrac
        self.ruka = []
        self.dobivene = []

class Briskula:
    bodovi = { 1: 11, 3: 10, 11: 2, 12: 3, 13: 4 } 
    snaga = { 1: 1, 3: 2, 13: 3, 12: 4, 11: 5 }
    
    def __init__(self, igrac1, igrac2):
        self.igrac1 = igrac1
        self.igrac2 = igrac2
        self.spil = Spil()
        self.briskula = ""
        self.stol = []
        self.stanje_igrac1 = StanjeIgraca(igrac1)
        self.stanje_igrac2 = StanjeIgraca(igrac2)
        self.prethodni_pobjednik = None
        
        
    def odredi_briskulu(self):
        self.briskula = self.spil.peskaj()
        self.spil.karte.append(self.briskula)
        
        
    def __str__(self):
        broj_karata_u_spilu = len(self.spil.karte) - 1 if len(self.spil.karte) > 0 else 0
        return (f"Broj karata u spilu: {broj_karata_u_spilu}\n"
                f"Briskula je: {self.briskula}\n"
                f"Karte na stolu: {self.stol}\n"
                f"Karte igraca {self.igrac1.ime}: {self.stanje_igrac1.ruka}\n"
                f"Karte igraca {self.igrac2.ime}: {self.stanje_igrac2.ruka}")
        
        
    def stanje(self, igrac):
        if igrac.ime == "igrac1":
            return {"briskula": self.briskula, "ruka":self.stanje_igrac1.ruka, "stol": self.stol, "dobivene":self.stanje_igrac1.dobivene, "dobivene_protivnik":self.stanje_igrac2.dobivene}
        elif igrac.ime == "igrac2":
            return {"briskula": self.briskula, "ruka":self.stanje_igrac2.ruka, "stol": self.stol, "dobivene":self.stanje_igrac2.dobivene, "dobivene_protivnik":self.stanje_igrac1.dobivene}
  
    
            
    def odigraj_ruku(self, prikaz=True):
        if self.prethodni_pobjednik == self.igrac2:
            akcija_igrac2 = self.igrac2.akcija(self.stanje(self.igrac2))
            karta_igrac2 = self.stanje_igrac2.ruka.pop(akcija_igrac2)
            self.stol.append(karta_igrac2)
            #print(self.stol)

            akcija_igrac1 = self.igrac1.akcija(self.stanje(self.igrac1))
            karta_igrac1 = self.stanje_igrac1.ruka.pop(akcija_igrac1)
            self.stol.append(karta_igrac1)
            #print(self.stol)
        else:
            akcija_igrac1 = self.igrac1.akcija(self.stanje(self.igrac1))
            karta_igrac1 = self.stanje_igrac1.ruka.pop(akcija_igrac1)
            self.stol.append(karta_igrac1)
            #print(self.stol)

            akcija_igrac2 = self.igrac2.akcija(self.stanje(self.igrac2))
            karta_igrac2 = self.stanje_igrac2.ruka.pop(akcija_igrac2)
            self.stol.append(karta_igrac2)
            #print(self.stol)
            
        prva_karta = self.stol[0]

        if prva_karta == karta_igrac1:
            druga_karta = karta_igrac2
        else:
            druga_karta = karta_igrac1

        if self.provjeri_jacinu(prva_karta, druga_karta, self.briskula):
            if prva_karta == karta_igrac1:
                self.stanje_igrac1.dobivene.append((karta_igrac1, karta_igrac2))
                self.prethodni_pobjednik = self.igrac1
            else:
                self.stanje_igrac2.dobivene.append((karta_igrac1, karta_igrac2))
                self.prethodni_pobjednik = self.igrac2
        else: 
            if prva_karta == karta_igrac1:
                self.stanje_igrac2.dobivene.append((karta_igrac1, karta_igrac2))
                self.prethodni_pobjednik = self.igrac2
            else:
                self.stanje_igrac1.dobivene.append((karta_igrac1, karta_igrac2))
                self.prethodni_pobjednik = self.igrac1

        if prikaz:
            if self.prethodni_pobjednik == self.igrac1:
                print(self.igrac1.ime, ":", karta_igrac1)
                print(self.igrac2.ime, ":", karta_igrac2)
            else:
                print(self.igrac2.ime, ":", karta_igrac2)
                print(self.igrac1.ime, ":", karta_igrac1)
        self.stol = []

    
    def provjeri_jacinu(self, igrac1_karta, igrac2_karta, briskula):
        karta1, znak1 = igrac1_karta
        karta2, znak2 = igrac2_karta
        
        if znak1 == znak2 == briskula[1]:
            if karta1 not in self.snaga and karta2 not in self.snaga:
                return True
            elif karta1 in self.snaga and karta2 in self.snaga:
                return self.bodovi.get(karta1, 0) > self.bodovi.get(karta2, 0)
            elif karta1 in self.snaga and karta2 not in self.snaga:
                return True
            else:
                return False
        elif znak1 == briskula[1] and znak2 != briskula[1]:
            return True
        elif znak2 == briskula[1] and znak1 != briskula[1]:
            return False
        elif (znak1 != briskula[1] and znak2 != briskula[1]):
            if znak1 == znak2:
                if karta1 in self.snaga and karta2 not in self.snaga:
                    return True
                elif karta1 not in self.snaga and karta2 in self.snaga:
                    return False
                elif karta1 not in self.snaga and karta2 not in self.snaga:
                    return True
                else:
                    return self.bodovi.get(karta1, 0) > self.bodovi.get(karta2, 0)
            else:
                return True
                    
                
    def odigraj_partiju(self, prikaz=True):
        self.spil.mijesaj_karte()
        self.stanje_igrac1.ruka = self.spil.dijeli_karte(3)
        self.stanje_igrac2.ruka = self.spil.dijeli_karte(3)
        self.odredi_briskulu()
        
        
        while len(self.stanje_igrac1.ruka) > 0 and len(self.stanje_igrac2.ruka) > 0:
            self.odigraj_ruku(prikaz)
            
            if self.spil.karte:
                self.stanje_igrac1.ruka.append(self.spil.peskaj())
                self.stanje_igrac2.ruka.append(self.spil.peskaj())
                #print("1",self.stanje(self.igrac1))
                #print("2",self.stanje(self.igrac2))

                
    def rezultat(self):
        igrac1_bodovi, igrac2_bodovi = 0, 0
        
        for value in self.stanje_igrac1.dobivene:
            for v in value:
                igrac1_bodovi += self.bodovi.get(v[0], 0)
                
        for value in self.stanje_igrac2.dobivene:
            for v in value:
                igrac2_bodovi += self.bodovi.get(v[0], 0)
                                    
        #print("Igrac1 bodovi:", igrac1_bodovi)
        #print("Igrac2 bodovi:", igrac2_bodovi)
                        
        if igrac1_bodovi > 60:
            return 1
        elif igrac2_bodovi > 60:
            return 2
        return 0


        
def main():
    igrac1 = Igrac("igrac1")
    igrac2 = Human("igrac2")
    briskula = Briskula(igrac1, igrac2)
    briskula.odigraj_partiju()
    print(briskula.rezultat())
    
if __name__ == '__main__':
    main()
    