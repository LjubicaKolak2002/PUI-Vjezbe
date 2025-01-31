import random

class Spil:
    def __init__(self):
        self.karte = self.generiraj_spil()
        
    
    def generiraj_spil(self):
        zogovi = ['K', 'S', 'B', 'D']
        brojevi = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13]
        spil = []
        
        for zog in zogovi:
            for broj in brojevi:
                spil.append((broj, zog))
        return spil
    
        
    def mijesaj_karte(self):
        random.shuffle(self.karte)
        
    def dijeli_karte(self, broj_karata):
        karte_u_ruci = []
        for _ in range(broj_karata):
            karta = self.karte.pop(0)
            karte_u_ruci.append(karta)
        return karte_u_ruci
    
    def peskaj(self):
       if self.karte:
            return self.karte.pop(0)
       else:
           print("Spil je prazan")
           
    

def main():
    spil = Spil()
    print(spil.generiraj_spil())
    spil.mijesaj_karte()
    print("\nNakon mjesanja: ",spil.karte)
    print("\n3 podijeljenje karte: ",spil.dijeli_karte(3))

if __name__ == '__main__':
    main()
    
                
        
        
          
        
        
        